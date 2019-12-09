using System;
using System.IO;

namespace _1
{
    class Program {
		static void Main(string[] args) {
			string input = File.ReadAllText(@"./input.txt");

			string[] inputs = input.Split( Environment.NewLine, StringSplitOptions.None ); 
			int[] output = new int[100];
			double input_;
			int sum = 0;
			for ( int i = 0; i < inputs.Length; i++ ) {
				Console.WriteLine( inputs[i] );
				input_ = Convert.ToDouble(inputs[i]);
				output[i] = (int)Math.Floor( input_/3 ) - 2;
				Console.WriteLine(output[i]);
				sum += output[i];
			}
			Console.WriteLine("Sum: " + sum.ToString() );
		}
	}
}
