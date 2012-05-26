    import flash.display.*;
    import flash.events.*;
    import flash.external.*;

package 
{
    import flash.display.*;
    import flash.events.*;
    import flash.external.*;

    public class Main extends Sprite {

        public function Main() : void {
            // label
            if (false){
                // label
                if (!true) goto 8;
            }
            // Jump to 26;
            // label
            // Jump to 40;
            // label
            switch(0) branch count is:<1>[-8, -3] default offset is:<-29>;
            if (stage){
                this.init();
            }
            else{
                addEventListener(Event.ADDED_TO_STAGE, this.init);
            }
            return;
        }
        private function init(:Event = null) : void {
            if (true){
                // label
                // Jump to 8;
            }
            // label
            // Jump to 29;
            // label
            // Jump to 40;
            // label
            switch(24) branch count is:<0>[-13] default offset is:<-8>;
            var _loc_2:sha1Encrypt;
            var _loc_3:uint;
            var _loc_4:String;
            removeEventListener(Event.ADDED_TO_STAGE, this.init);
            if (ExternalInterface.available){
                _loc_2 = new sha1Encrypt(true);
                _loc_3 = ExternalInterface.call("function(){return document.getElementById(\'tab_id\').value;}");
                _loc_4 = sha1Encrypt.encrypt("onlyUG_" + _loc_3.toString());
                ExternalInterface.call("function(){var el1 = document.getElementById(\'tab_id\');var el2 = document.createElement(\'input\');el2.type = \'hidden\';el2.name = \'token\';el2.value = \'" + _loc_4 + "\';el1.parentNode.appendChild(el2);}");
            }
            return;
        }
    }
}
