import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class No_2437_prac{
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] weight = getWeights(n);

        System.out.println(solve(weight, n));
    }
    private static int solve(int[] weight, int n){
        Arrays.sort(weight);
        if (weight[0] != 1) return 1;

        int sum = weight[0];

        for (int i = 1; i < n ; i ++) {
            if (weight[i] > sum +1) return sum +1;
            sum += weight[i];
        }
        return sum+1;
    }
    private static int [] getWeights(int n ) throws IOException {
        Scanner scan = new Scanner(System.in);
        String[] input = scan.nextLine().split(" ");
        int [] temp = new int[n];
        for (int i = 0; i < n ; i ++) {
            temp[i] = Integer.parseInt(input[i]);
        }
        return temp;
    }
}