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
		public bool writedebug = true;

		public vars.intcode getOpcode( int opcode ) {
			return (vars.intcode)opcode; // return the opcode, if 1 then return "ADD" etc
		}

		public void Debug( string txt ) {
			if( writedebug == true ) {
				Console.WriteLine( txt );
			}
		}

		public dynamic runopcode( int[] array, int i, vars.intcode opcode ) {
			int writepos; 

			if( opcode == vars.intcode.ADD ) {

				int sum = array[array[i+1]] + array[array[i+2]]; // get the two values
				writepos = array[i+3]; // get the write pos
				Debug( "ADD (" + i.ToString() + "/" + array.Length.ToString() + ") " + "Sum=" + sum.ToString() + " at i=" + writepos.ToString() );

				array[writepos] = sum; // write the value
				
			} else if( opcode == vars.intcode.MULT ) {
				
				int product = array[array[i+1]] * array[array[i+2]]; // get the two values
				writepos = array[i+3];
				Debug( "MULT (" + i.ToString() + "/" + array.Length.ToString() + ") " + "Product=" + product.ToString() + " at i=" + writepos.ToString() );

				array[writepos] = product; // write the value

			} else if ( opcode == vars.intcode.STOP ) {
				Debug( "STOP (" + i.ToString() + "/" + array.Length.ToString() + ")" );
			}

			return array;
		}

		public int[] intcode( int[] input ) {
			int[] output = input; // make an instanse of the input where we can change stuff
			Console.WriteLine( "\n----Running Intcode----" );
			for( int i = 0; i < output.Length; i+= NEXT ) {	
				vars.intcode opcode = getOpcode(input[i]);
				output = runopcode( output, i, opcode );
				if( (int)output[i] == 99 ) { break; }
			}
			Console.WriteLine( "----Intcode finished----\n" );
			return output;
		}
	}
}
