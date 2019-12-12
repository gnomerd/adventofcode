using System;
using System.IO;
using System.Collections.Generic;

namespace Day1 {
    class Program {
		static void Main(string[] args) {
			string input = File.ReadAllText(@"./input.txt"); // get the input

			string[] inputs = input.Split( Environment.NewLine, StringSplitOptions.None ); 
			int[] modules = new int[inputs.Length];


			Part1.Get get1 = new Part1.Get();
			modules = get1.FuelModules( inputs ); // get the fuel for the mass'es
			Console.WriteLine( get1.FuelSum( modules ) );

			//int[,] modulesOfModules = new int[,];
			Part2.Get get2 = new Part2.Get();
			Console.Write( "Real sum: " );
			Console.Write( get2.addAllArray( get2.AllFuelModules( modules ) ) );
			Console.WriteLine("");

		}
	}
}
