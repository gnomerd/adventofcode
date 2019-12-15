using System;
using System.IO;

namespace Day2 {
	class Program {
		static void Main(string[] args) {
			string input = File.ReadAllText(@"./input.txt"); // get the input

			string[] inputs = input.Split( ",", StringSplitOptions.None );
			int[] intcodes = Array.ConvertAll( inputs, str => int.Parse( str ) ); // convert all of the contents to int's

			int[] output = new int[intcodes.Length];

			Part1.compile compile = new Part1.compile();

			//// Part 1 stuff ////
			intcodes[1] = 12;
			intcodes[2] = 2;

			output = compile.intcode( intcodes, false ); // run the intcode program

			Console.WriteLine("\n--Intcode result--");
			for( int i = 0; i < output.Length; i++ ) {
				if( i != output.Length - 1 ) {
					Console.Write( output[i].ToString() + "," );
				} else {
					Console.Write( output[i].ToString() + "\n" );
				}
			}
			Console.WriteLine( "--End of Intcode result--\n" );

			Console.WriteLine( "Part 1 result: " + output[0].ToString() ); // get the pos 0



			//// Part 2 stuff ////
			Part2.calcInputs calcInputs = new Part2.calcInputs();
			int[] intcodes2 = intcodes; // make a new instance of it
			int res;
			res = calcInputs.bruteforce( intcodes2, 19690720, false );
			Console.WriteLine( "Part 2 Result: {0}", res );
		}
	}
}
