import java.lang.Math;
import java.math.BigDecimal;

public class IsItTheFlag {

	public static boolean isFlag(String str) {
		return str.hashCode() == 1471587914 && str.toLowerCase().hashCode() == 1472541258;
	}

	public static void main(String[] args) {

		String flag = "------";
		String alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
		char[] alphabet = alph.toCharArray();
		int alphabet_l = alphabet.length;

		int[] pos = {0, 0, 0, 0, 0, 0};
		System.out.println("alphabet length: " + alphabet_l);

		double numToCheck = Math.pow(alphabet_l, pos.length);
		System.out.println("total-bruteforce: " + numToCheck);

		long counter = 0;
		long startMillies = System.currentTimeMillis();
		while(true) {
			flag = "" + alphabet[pos[0]] + alphabet[pos[1]] + alphabet[pos[2]] + alphabet[pos[3]] + alphabet[pos[4]] + alphabet[pos[5]];
		
			//System.out.println(flag);

			if (isFlag(flag)) {
				System.out.println("You found it! [" + flag + "])");
				break;
			}

			for (int i = 0; i < pos.length; i++) {
				if (pos[i] >= alphabet_l - 1) {
					pos[i] = 0;
				} else {
					pos[i]++;
					break;
				}
			}
			counter++;
			if(counter % 100000000 == 0) {
				long timeTaken = System.currentTimeMillis() - startMillies;
				double currentPercentDone = counter / numToCheck;
				System.out.printf("still %-11s to go ... currently at %s, eta for all permutations: %.0f seconds (%d per second) %n", new BigDecimal(numToCheck - counter).toString(), flag, ((1 - currentPercentDone) / currentPercentDone) * timeTaken / 1000, counter/timeTaken*1000);
			}
			if(counter >= numToCheck) {
				System.out.printf("nothing found, currently at %s%n", flag);
				break;
			}
		}
	}
}
