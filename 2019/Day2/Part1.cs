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
		public int NEXT = 4; // steps per opcode

		public vars.intcode getOpcode( int opcode ) {
			return (vars.intcode)opcode; // return the opcode, if 1 then return "ADD" etc
		}

		public bool isOpcode( int i ) {
			return false;
		}

		public int[] runopcode( int[] array, int i, vars.intcode opcode ) {
			int writepos = array[array[i+3]]; // get the write pos

			if( opcode == vars.intcode.ADD ) {
				int sum = array[array[i+1]] + array[array[i+2]]; // get the two values
				Console.WriteLine( "ADD (" + i.ToString() + ") " + "Sum=" + sum.ToString() + " at i=" + array[i+3].ToString() );
				array[writepos] = sum; // write the value
				
			} else if( opcode == vars.intcode.MULT ) {
				int product = array[array[i+1]] * array[array[i+2]]; // get the two values
				Console.WriteLine( "MULT (" + i.ToString() + ") " + "Product=" + product.ToString() + " at i=" + array[i+3].ToString() );
				array[writepos] = product; // write the value
			} else if ( opcode == vars.intcode.STOP ) {

			}

			return array;
		}

		public int[] intcode( int[] input ) {
			int[] output = input; // make an instanse of the input where we can change stuff
			//int opcode_count = 0;
			for( int i = 0; i < output.Length; i+= NEXT ) {
				
				Console.WriteLine(i);
				vars.intcode opcode = getOpcode(input[i]);
				output = runopcode( output, i, opcode );
				
				//Console.WriteLine( getOpcode(output[i]).ToString() + " | " + i.ToString() );
			}
			return output;
		}
	}
}
