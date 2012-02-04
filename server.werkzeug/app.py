import os
import urlparse
import redis
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader

class App(object):
    def __init__(self, config):
        self.redis = redis.Redis(config['redis_host'], config['redis_port'])
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)
        self.url_map = Map([
            Rule('/', endpoint='root'),
            Rule('/<short_id>', endpoint='link'),
            Rule('/<short_id>+', endpoint='link_details'),
            Rule('/api/base36_encode/<string>', endpoint='api_base36_encode'),
        ])

    def on_root(self, request, **values):
        error = None
        target = ''
        if request.method == 'POST':
            target = request.form['target']
            if not self.is_valid_url(target):
                error = 'Must be a HTTP or HTTPS address.'
            else: 
                short_id = self.insert_new_target(target)
                return redirect('/%s+' % short_id)
        return self.render_template('new_url.html', error=error, target=target)

    def on_link(self, request, **values):
        short_id = values['short_id']
        target = self.redis.get('short_id:'+short_id)
        if target is not None:
            return redirect(target)
        raise NotFound

    def on_link_details(self, request, **values):
        short_id = values['short_id']
        target = self.redis.get('short_id:'+short_id)
        if target is not None:
            return self.render_template('link_details.html', short_id=short_id, target=target)
        raise NotFound

    def on_api_base36_encode(self, request, **values):
        base10 = int(values['string'])
        base36 = base36_encode(base10)
        out = 'base10=%s\nbase36=%s'  % (base10, base36)
        return Response(out)

    def is_valid_url(self,target):
        parts = urlparse.urlparse(target)
        return parts.scheme in ('http','https')

    def insert_new_target(self,target):
        short_id = self.redis.get('target:'+target)
        if short_id is not None:
            return short_id
        url_num = self.redis.incr('last-url-id')
        short_id = base36_encode(url_num)
        self.redis.set('target:'+target,short_id);
        self.redis.set('short_id:'+short_id,target);
        return short_id

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        rendered = t.render(context)
        return Response(rendered, mimetype='text/html')

    def dispatch_request(self,request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self,'on_'+endpoint)(request,**values)
        except HTTPException, e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

def create_app(redis_host='localhost', redis_port=6379, with_static=True):
    app = App({
        'redis_host': redis_host,
        'redis_port': redis_port,
    })
    if with_static: 
        static_root = os.path.join(os.path.dirname(__file__), 'static')
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
               '/css': os.path.join(static_root, 'css'),
                '/js': os.path.join(static_root, 'js'),
            '/images': os.path.join(static_root, 'images'),
        })
    return app

def base36_encode(num):
    assert num>=0, 'positive integer required'
    if num == 0: return '0'
    out = []
    while num>0:
        num, mod = divmod(num,36)
        out.append('0123456789abcdefghijklmnopqrstuvwxyz'[mod])
    return ''.join(reversed(out))

