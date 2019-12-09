using System;
using System.IO;

namespace Day1 {
    class Program {
		static void Main(string[] args) {
			string input = File.ReadAllText(@"../input.txt"); // get the input

			string[] inputs = input.Split( Environment.NewLine, StringSplitOptions.None ); 
			int[] modules = new int[100];

			Part1.Get get = new Part1.Get();
			modules = get.FuelModules( inputs ); // get the fuel for the mass'es
			Console.WriteLine( get.FuelSum( modules ) );
		}
	}
}
