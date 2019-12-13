using System;

namespace Part2 {
	public class calcInputs {
		public void bruteforce( int[] input, int find ) {
			int noun, verb;
			int[] input_c = input; // keep a version of the original
			int[] output = new int[input_c.Length];

			bool success = false;

			int min = 0;	// min and max for the input values
			int max = 99;	//

			Part1.compile compile = new Part1.compile();

			for( int i = 0; i < max + 1; i++ ) {
				input = input_c; // reset the intcode

				noun = Math.Clamp( i, min, max );
				verb = Math.Clamp( i, min, max );

				input[1] = noun;
				input[2] = verb;

				Console.WriteLine( "Checking: {0}, {1} for {2}", noun, verb, find );
				output = compile.intcode( input );

				Console.WriteLine( input[0] );
				if( output[0] == find ) {
					Console.WriteLine( "({0}) Found: {1}, {2}", find, noun, verb );
					success = true;
					break;
				}
				
			}

			Console.WriteLine("");

			if( success == false ) {
				Console.WriteLine( "Nothing found :(" );
				return;
			}
		}
	}
}