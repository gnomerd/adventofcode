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
			compile.intcode( intcodes );

		}
	}
}
