using System;
using System.IO;

namespace _1 {

	public class Part1 {
		public int[] GetFuelModules( string[] inputs ) {
			int[] output = new int[100];
			double input_;
			for ( int i = 0; i < inputs.Length; i++ ) {
				input_ = Convert.ToDouble(inputs[i]);
				output[i] = (int)Math.Floor( input_/3 ) - 2; // do the fuel calc
				Console.WriteLine(output[i]);
			}
			return output;
		}
	}
    class Program {

		
		static void Main(string[] args) {
			string input = File.ReadAllText(@"../../input.txt"); // get the input

			string[] inputs = input.Split( Environment.NewLine, StringSplitOptions.None ); 
			int[] modules = new int[100];

			Part1 prt1 = new Part1();
			modules = prt1.GetFuelModules( inputs ); // get the fuel for the mass'es

			int sum = 0;
			for( int i = 0; i < modules.Length; i++ ) { sum += modules[i]; } // add all of the fuel

			Console.WriteLine("Sum: " + sum.ToString() ); //output the answer
		}
	}
}
