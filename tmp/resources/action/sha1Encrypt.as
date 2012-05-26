
package 
{

    public class sha1Encrypt extends Object {
        private static var charInputBit:uint;

        public function sha1Encrypt(:Boolean) {
            // label
            // Jump to 26;
            if (false){
                // label
                // Jump to 21;
            }
            else{
                // label
                // Jump to 37;
                // label
                switch(125) branch count is:<0>[-3] default offset is:<-8>;
                if (){
                    charInputBit = 8;
                }
                else{
                    charInputBit = 16;
                }
                return;
            }
        }
        private static function string_to_bin(:String) : Array {
            // label
            if (false){
                // label
                // Jump to 17;
            }
            else{
                // Jump to 26;
                // label
                // Jump to 37;
                // label
                switch(23) branch count is:<0>[-29] default offset is:<-8>;
                var _loc_2:* = new Array();
                var _loc_4:Number;
                while (_loc_4 < length * charInputBit){
                    // label
                    _loc_2[_loc_4 >> 5] = _loc_2[_loc_4 >> 5] | (charCodeAt(_loc_4 / charInputBit) & (1 << charInputBit)--) << 32 - charInputBit - _loc_4 % 32;
                    _loc_4 = _loc_4 + charInputBit;
                }
                return _loc_2;
            }
        }
        public static function encrypt(:String) : String {
            // label
            if (!true){
                // label
                // Jump to 16;
            }
            else{
                // Jump to 25;
                // label
                // Jump to 36;
                // label
                switch(0) branch count is:<0>[-8] default offset is:<-28>;
                return hex_sha1();
            }
        }
        private static function sha_f_mod(:Number, :Number, :Number, :Number) : Number {
            // label
            if (false){
                // label
                // Jump to 19;
            }
            else{
                // Jump to 28;
                // label
                // Jump to 42;
                // label
                switch(-73) branch count is:<1>[-30, -3] default offset is:<-8>;
                if ( < 20){
                    return  &  | ~ & ;
                }
                if ( < 40){
                    return  ^  ^ ;
                }
                if ( < 60){
                    return  &  |  &  |  & ;
                }
                return  ^  ^ ;
            }
        }
        private static function bin_to_hex(:Array) : String {
            if (true){
                // label
            }
            // label
            // Jump to 29;
            // label
            // Jump to 40;
            // label
            switch(0) branch count is:<0>[-8] default offset is:<-13>;
            var _loc_2:String;
            var _loc_3:* = new String();
            var _loc_4:Number;
            while (_loc_4++ < length * 4){
                // label
                _loc_3 = _loc_3 + (_loc_2.charAt([_loc_4 >> 2] >> (3 - _loc_4 % 4) * 8 + 4 & 15) + _loc_2.charAt([_loc_4 >> 2] >> (3 - _loc_4 % 4) * 8 & 15));
            }
            return _loc_3;
        }
        private static function sha1_convert(:Array, :Number) : Array {
            // label
            if (true){
                // label
                // Jump to 9;
            }
            // Jump to 27;
            // label
            // Jump to 38;
            // label
            switch(0) branch count is:<0>[-8] default offset is:<-3>;
            var _loc_10:Number;
            var _loc_11:Number;
            var _loc_12:Number;
            var _loc_13:Number;
            var _loc_14:Number;
            var _loc_15:Number;
            var _loc_16:Number;
            var _loc_3:Number;
            var _loc_4:Number;
            var _loc_5:Number;
            var _loc_6:Number;
            var _loc_7:Number;
            var _loc_8:* = new Array();
            [ >> 5] = [ >> 5] | 128 << 24 -  % 32;
            [( + 64 >> 9 << 4) + 15] = ;
            var _loc_9:Number;
            while (_loc_9 < length){
                // label
                _loc_10 = _loc_3;
                _loc_11 = _loc_4;
                _loc_12 = _loc_5;
                _loc_13 = _loc_6;
                _loc_14 = _loc_7;
                _loc_15 = 0;
                while (_loc_15++ < 80){
                    // label
                    if (_loc_15 < 16){
                        _loc_8[_loc_15] = [_loc_9 + _loc_15];
                    }
                    else{
                        _loc_8[_loc_15] = rol(_loc_8[_loc_15 - 3] ^ _loc_8[_loc_15 - 8] ^ _loc_8[_loc_15 - 14] ^ _loc_8[_loc_15 - 16], 1);
                    }
                    _loc_16 = safe_add(safe_add(rol(_loc_3, 5), sha_f_mod(_loc_15, _loc_4, _loc_5, _loc_6)), safe_add(safe_add(_loc_7, _loc_8[_loc_15]), sha_z_mod(_loc_15)));
                    _loc_7 = _loc_6;
                    _loc_6 = _loc_5;
                    _loc_5 = rol(_loc_4, 30);
                    _loc_4 = _loc_3;
                    _loc_3 = _loc_16;
                }
                _loc_3 = safe_add(_loc_3, _loc_10);
                _loc_4 = safe_add(_loc_4, _loc_11);
                _loc_5 = safe_add(_loc_5, _loc_12);
                _loc_6 = safe_add(_loc_6, _loc_13);
                _loc_7 = safe_add(_loc_7, _loc_14);
                _loc_9 = _loc_9 + 16;
            }
            return [_loc_3, _loc_4, _loc_5, _loc_6, _loc_7];
        }
        private static function hex_sha1(:String) : String {
            if (!true){
                // label
                // Jump to 7;
            }
            // label
            // Jump to 27;
            // label
            // Jump to 41;
            // label
            switch(112) branch count is:<1>[-13, -3] default offset is:<-8>;
            return bin_to_hex(sha1_convert(string_to_bin(), length * charInputBit));
        }
        private static function sha_z_mod(:Number) : Number {
            if (!true){
                // label
                // Jump to 8;
            }
            // label
            // Jump to 28;
            // label
            // Jump to 42;
            // label
            switch(0) branch count is:<1>[-8, -13] default offset is:<-3>;
            return  < 20 ? (1518500249) : ( < 40 ? (1859775393) : ( < 60 ? (-1894007588) : (-899497514)));
        }
        private static function rol(:Number, :Number) : Number {
            // label
            // Jump to 25;
            if (true){
                // label
            }
            // label
            // Jump to 39;
            // label
            switch(1) branch count is:<1>[-28, -8] default offset is:<-3>;
            return  <<  |  >>> 32 - ;
        }
        private static function safe_add(:Number, :Number) : Number {
            if (true){
                // label
                // label
                // label
            }
            // label
            // Jump to 29;
            // label
            // Jump to 43;
            // label
            switch(1) branch count is:<1>[-13, -8] default offset is:<-3>;
            var _loc_3:* = ( & 65535) + ( & 65535);
            var _loc_4:* = ( >> 16) + ( >> 16) + (_loc_3 >> 16);
            return ( >> 16) + ( >> 16) + (_loc_3 >> 16) << 16 | _loc_3 & 65535;
        }
    }
}
