using System;
using System.IO;

namespace Part1 {
	public class vars{
		public enum intcode : int {
			ADD = 1,
			MULT = 2,
			STOP = 99
		}
		public int NEXT = 4; // steps per opcode
	}
	public class compile {
		public vars.intcode getOpcode( int opcode ) {
			return (vars.intcode)opcode; // return the opcode, if 1 then return "ADD" etc
		}

		public void runopcode( int index, vars.intcode opcode ) {
			if( opcode == vars.intcode.ADD ) {

			}
		}

		public int[] intcode( int[] input ) {
			int[] output = input; // make an instanse of the input where we can change stuff
			for( int i = 0; i < input.Length; i++ ) {
				vars.intcode opcode = getOpcode(input[i]);
				//Console.WriteLine( getOpcode(input[i]).ToString() + " | " + i.ToString() );
				runopcode( i, opcode );
			}
			return output;
		}
	}
}
