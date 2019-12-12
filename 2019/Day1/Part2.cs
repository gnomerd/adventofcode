using System;
using System.Data;

namespace Part2 {
	public class Get {
		public int[,] AllFuelModules( int[] modules ) {
			
			// declare the variables
			int[,] returnarray = new int[modules.Length, 999]; // make a 2D array, 999 is a bit overkill but it will work I guess

			for( int i = 0; i < modules.Length; i++ ) { // loop through each module
				// i = module index
				returnarray[i, 0] = modules[i]; // set the first to be the module
				for( int mod_i = 1; returnarray[i, mod_i - 1] > 0; mod_i++ ) { // start at the second since we declared the first one above
					returnarray[i, mod_i] = (int)Math.Floor( (float)returnarray[i, mod_i - 1] / 3 ) - 2;
					if( returnarray[i, mod_i] < 0 ) { returnarray[i, mod_i] = 0; } // if less than 0 then just make it 0
				}
			}

			return returnarray; // return the complete array
		}

		public int addAllArray( int[,] array ) {
			int sum = 0;
			for( int i = 0; i < array.GetLength(0); i++ ) {
				for( int mod_i = 0; mod_i < array.GetLength(1); mod_i++ ) {
					sum += array[i, mod_i];
				}
			}
			return sum;
		}
	}
}
