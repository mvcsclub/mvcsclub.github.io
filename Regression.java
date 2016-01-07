/**
* MVCS Club
* January 6, 2015
*
* A program that calculates a basic linear regression
*/


public class Regression {
	public static void main(String[] args) {
		double m = 0.0;
		double bestM = 0.0;
		double bestError = 100000.0;
		double[] x = {11.0, 8.0, 0.5, 7.5};
		double[] y = {4.0, 3.5, 3.2, 3.0};
		for(int i = 0; i < 10000000; i++) {
			m = Math.random()*5;
			double error = 0;	
			for(int j = 0; j < x.length; j++) {
				error += (m*x[j] - y[j])*(m*x[j] - y[j]);
			}
			if(error < bestError) {
				bestM = m;
				bestError = error;
			}
		}
		System.out.println(bestM);
	}
}
