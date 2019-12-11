using System;
using System.Collections.Generic;

namespace Part2 {
	public class Get {
		public List<int[]> AllFuelModules( int[] modules ) {
			
			// declare the variables
			List<int[]> returnList = new List<int[]>();
			int[] modulesofmodule = new int[999]; // should be big enough xd
			float mod;
			int placeholder;

			int count = -1; // dumb method ikr
			
			for( int i = 0; i < modules.Length; i++ ) { // loop through the modules
				Console.WriteLine("----");
				mod = (float)modules[i]; // make it a double
				placeholder = (int)mod; 

				//modulesofmodule[count] = (int)mod;

				while( placeholder > 0 ) { // if the placeholder is greater than 0
					count++;
					
					placeholder = (int)Math.Floor( mod/3 ) - 2; // then do the fuel calc for the fuel module
					
					if( placeholder < 0 ) { // if less than 0 then just make it 0
						placeholder = 0;
						modulesofmodule[count] = (int)placeholder; // add it to its own little list
					} else {
						modulesofmodule[count] = (int)placeholder; // same here
					}
					Console.WriteLine( count.ToString() + " val: " + placeholder.ToString() );
					
				}
				count = -1; // reset the count
				Console.WriteLine( "ID: " + i.ToString() );
				returnList.Add( modulesofmodule ); // place the array in the list for that module
			}

			return returnList; // return the complete list
		}

		public int RealFuelSum( List<int[]> fuelmodules ) {
			int sum = 0;
			for( int arrayid = 0; arrayid < fuelmodules.Count; arrayid++ ) {
				for( int i = 0; i < fuelmodules[arrayid].Length; i++ ) {
					sum += fuelmodules[arrayid][i];
					//Console.WriteLine( "Module " + arrayid.ToString() + "/" + fuelmodules.Count.ToString() + " | " + i.ToString() + "/" + fuelmodules[arrayid].Length.ToString() + " | val: " + fuelmodules[arrayid][i].ToString() );
				}
			}
			return sum;
		}
	}
}
