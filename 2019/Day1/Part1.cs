using System;
using System.IO;

namespace Part1 {

	public class Get {
		public int[] FuelModules( string[] inputs ) {
			int[] output = new int[100];
			double input_;
			for ( int i = 0; i < inputs.Length; i++ ) {
				input_ = Convert.ToDouble(inputs[i]);
				output[i] = (int)Math.Floor( input_/3 ) - 2; // do the fuel calc
			}
			return output;
		}

		public int FuelSum( int[] modules ) {
			int sum = 0;
			for( int i = 0; i < modules.Length; i++ ) { sum += modules[i]; } // add all of the fuel
			return sum;
		}
	}
}
