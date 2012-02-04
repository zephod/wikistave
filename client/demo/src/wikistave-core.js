
var App = App || {};
App.Util = App.Util || {};
App.Model = App.Model || {};
App.View = App.View || {};

// Model: Note
App.Model.Note = Backbone.Model.extend({
  defaults: { 
    line: 3,
    duration: 256,
    rest: false
  },
  pitchUp: function() {
    this.set('line', this.get('line')-1);
  }
});

// Model: Stave
App.Model.Stave = Backbone.Model.extend({
  initialize: function() {
    this.notes.bind('all', function(e) { this.change(e); }, this);
  },
  // A key into the stave vector hashset
  defaults: {
    clefName: null
  },
  // A collection of Note models
  notes: new (Backbone.Collection.extend({ model: App.Model.Note }))()
});

// View: Stave 
App.View.Stave = Backbone.View.extend({
  initialize: function() {
    if (!this.options.clefSpace) {
      var defaultSpace = this.options.h / 8;
      this.options.clefSpace = defaultSpace;
    }
    this.model.bind('change',this.render,this);
    this.noteVectors = [];
    this.render();
  },
  // Use this to change the position of the stave and
  // automatically trigger a re-render.
  setPosition: function(obj) {
    _.extend(this.options, obj);
    this.render();
  },
  render: function() {
    // Remove previous vectors
    if (this.clef) this.clef.remove();
    if (this.stave) this.stave.remove();
    var context = this;
    _.each(this.noteVectors, function(vector) {
      vector.remove();
    });
    this.noteVectors=[];
    
    // Shortcut to the options object
    var o = this.options;
    // Render the stave
    var spacing = o.h/4;
    var stavePath = '';
    for (var i=0;i<5;i++) {
      stavePath += ['M', o.x, (Math.round(o.y+i*spacing)+0.5), 'h', o.w ];
    }
    this.stave = App.paper.path(stavePath);

    // Render the stave's clef
    var clefPath = App.Vectors.clef.path[this.model.get('clefName')];
    if (clefPath) {
      var scale = o.h / App.Vectors.clef.h;
      this.clef = App.paper.path(clefPath).attr(App.Util.blackFill);
      this.clef.translate(
        o.x+(App.Vectors.clef.w*scale/2)+o.clefSpace, 
        o.y+(o.h/2));
      this.clef.scale(scale,scale,0,0);
    }

    // Render the string of notes
    var note_x = o.x+o.clefSpace+(App.Vectors.clef.w*scale)+(2*spacing);
    var note_step = (2.3 * spacing);
    var spot = 6;
    var line = 10;
    this.model.notes.each(function(note) {
      var note_y = o.y + spacing*(note.get('line')-1);
      var obj = note.get('line')>2 ? App.Vectors.crotchetUp : App.Vectors.crotchetDown;
      if (note.get('rest')) obj = App.Vectors.crotchetRest;
      var noteVector = new App.Vectors.Vector(obj);
      noteVector.moveTo(note_x, note_y);
      noteVector.setScale(obj.h / 256);
      context.noteVectors.push(noteVector.vector);
      note_x += note_step;
    });
  }
});

// Utility: Attributes to fill the clef
App.Util.blackFill = {stroke:'none',fill:'#000'};
App.Util.redLines = {stroke:'#f00'};

// On document ready, create the application
$(function() {
  App.paper = Raphael("holder", 800, 380);

  var pos = new Backbone.Model({ a: 1});

  var staveModel = new App.Model.Stave({
    clefName: 'g'
  });

  var staveView = new App.View.Stave({ 
    x: 10, 
    y: 120, 
    w: 800, 
    h: 60, 
    model: staveModel
  });

  $('button.js-note').click(function(e) {
    var value = e.target.value;
    if (value=='rest') {
      console.log(asdf);
      staveModel.notes.add({rest: true});
    }
    else if (value=='start over') {
      staveModel.notes.reset();
    }
    else {
      staveModel.notes.add({line: value});
    }
  });
  $('input.js-clef').click(function(e) {
    var value = e.target.value;
    staveModel.set({clefName: value});
    $('div.js-clef').hide();
    $('div.js-clef.'+value).css({display:'inline'});
    staveModel.notes.reset();
  });
});


