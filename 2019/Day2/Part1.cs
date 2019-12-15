using System;
using System.IO;

namespace Part1 {
	public class vars{
		public enum intcode : int {
			ADD = 1,
			MULT = 2,
			STOP = 99
		}
	}
	public class compile {
		public const int NEXT = 4; // steps per opcode
		public bool writedebug = !false;

		public vars.intcode getOpcode( int opcode ) {
			return (vars.intcode)opcode; // return the opcode, if 1 then return "ADD" etc
		}

		public void Debug( string txt ) {
			if( writedebug == true ) {
				Console.WriteLine( txt );
			}
		}

		public dynamic runopcode( int[] array, int i, vars.intcode opcode ) {
			int[] output = array;					// CREATE NEW INSTANCE 
			int writepos = output[i+3];
			int mod1 = output[ output[i+1] ];
			int mod2 = output[ output[i+2] ];

			if( writepos >= output.Length ) {
				Console.WriteLine( "[Warning] Tried to write at non-existent address ({0}/{1})", writepos, output.Length );
				writepos = output.Length - 1; // just write it at the end of the program
			}

			Console.WriteLine( "Mod1: {0}, Mod2: {1}, Writepos: {2}, mod1loc: {3}, mod2loc: {4}", mod1, mod2, writepos, output[i+1], output[i+2] );

			if( opcode == vars.intcode.ADD ) {

				Debug( "ADD (" + i.ToString() + "/" + output.Length.ToString() + ") " + "Sum=" + (mod1 + mod2).ToString() + " at i=" + writepos.ToString() );
				output[writepos] = mod1 + mod2; // write the value
				
			} else if( opcode == vars.intcode.MULT ) {

				Debug( "MULT (" + i.ToString() + "/" + output.Length.ToString() + ") " + "Product=" + (mod1 * mod2).ToString() + " at i=" + writepos.ToString() );
				output[writepos] = mod1 * mod2; // write the value

			} else if ( opcode == vars.intcode.STOP ) {
				Debug( "STOP (" + i.ToString() + "/" + output.Length.ToString() + ")" );
			}

			return output;
		}

		public int[] intcode( int[] input ) {
			int[] output = input; // make an instanse of the input where we can change stuff

			Console.Write( "\nRunning: " );
			for( int c = 0; c < input.Length; c++ ){ Console.Write( input[c].ToString() + "," ); }

			Debug( "\n----DEBUG----" );
			for( int i = 0; i < output.Length; i+= NEXT ) {	
				if( i+3 < output.Length ) {
					vars.intcode opcode = getOpcode(input[i]);
					output = runopcode( output, i, opcode );
				}
				if( (int)output[i] == 99 ) { break; }
			}
			Debug( "----END-OF-DEBUG----\n" );
			return output;
		}
	}
}
