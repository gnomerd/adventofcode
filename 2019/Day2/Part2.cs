using System;

namespace Part2 {
	public class calcInputs {
		public int bruteforce( int[] input, int find, bool debug ) {
			int noun, verb;
			int[] input_c; // keep a version of the original
			int[] output = new int[input.Length];

			bool success = false;

			int min = 0;	// min and max for the input values
			int max = 99;	//
			int maxcombos = Convert.ToInt16( Math.Pow( (double)(max + 1), 2.0 ) );

			Part1.compile compile = new Part1.compile();

			Console.WriteLine("Bruteforcing...");
			for( int c = 0; c < max + 1; c++ ) {
				noun = Math.Clamp( c, min, max );
				// check every verb with c (the noun)
				for( int i = 0; i < max + 1; i++ ) {
					input_c = input; // reset the intcode
					verb = Math.Clamp( i, min, max );

					input_c[1] = noun;
					input_c[2] = verb;

					output = compile.intcode( input_c, debug );

					if( output[0] == find ) {
						Console.WriteLine( "\n({0}) Found: {1}, {2}", find, noun, verb );
						success = true;
						return (100 * noun) + verb;
					}
				}

				if( success == true ) { break; }
			}

			Console.WriteLine("");

			if( success == false ) {
				Console.WriteLine( "Nothing found :(" );
				return -1;
			}
			return -1;
		}
	}
}