using System;

namespace Part2 {
	public class calcInputs {
		public void bruteforce( int[] input, int find ) {
			int noun, verb;
			int[] input_c; // keep a version of the original
			int[] output = new int[input.Length];

			bool success = false;

			int min = 0;	// min and max for the input values
			int max = 6;	//

			Part1.compile compile = new Part1.compile();

			for( int i = 0; i < max + 1; i++ ) {
				input_c = input; // reset the intcode

				noun = Math.Clamp( i, min, max );
				verb = Math.Clamp( i, min, max );

				input_c[1] = noun;
				input_c[2] = verb;

				output = compile.intcode( input_c );

				Console.WriteLine( input_c[0] );
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