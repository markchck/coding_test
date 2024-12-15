import java.util.ArrayList;
import java.util.Arrays;

public class 땅따먹기 {
    public static void main(String[] args) {

        public int solution( int[][] land) {


            int N = land.length;

//            ArrayList< int [] > dp = new ArrayList<>(N);



            for (int i = 0; i < N; i++){
                dp[i] = new int[4];
                // dp의 모든 인자를 0으로 초기화 한다.
                Arrays.fill(dp[i], 0);
            }

            // dp[0]은 land[0]과 같으므로 land[0]으로 초기화
            for(int i = 0; i<4; i++) {
                dp[0][i] = land[0][i];
            }


            // 반복이 필요함
            // 이중 for문을 돌리는데 첫번째 for문은 N-1번 돌리고 두번째 for문은 4번 돌린다. (i=1), (j=0)라고 할게. (0행은 초기화 되어있으니 i는 1부터)
            for (int i=1; i<N; i++){
                for (int j=0; j<4; j++){
                    // if (j ==0) dp[i][j] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3]) + land[i][j]
                    if(j==0){
                        dp[i][j] = maxNumber(dp[i-1][1], dp[i-1][2], dp[i-1][3]) + land[i][j];
                    }
                    // if (j ==1) dp[i][j] = max(dp[i-1][0], dp[i-1][2], dp[i-1][3]) + land[i][j]
                    if(j==1){
                        dp[i][j] = maxNumber(dp[i-1][0], dp[i-1][2], dp[i-1][3]) + land[i][j];
                    }
                    // if (j ==2) dp[i][j] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3]) + land[i][j]
                    if(j==2){
                        dp[i][j] = maxNumber(dp[i-1][0], dp[i-1][1], dp[i-1][3]) + land[i][j];
                    }
                    // if (j ==3) dp[i][j] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + land[i][j]
                    if(j==3){
                        dp[i][j] = maxNumber(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + land[i][j];
                    }
                }
            }
            int answer = 0;
            // return max(dp[N])
            for (int i =0; i<4; i++) {
                answer = Math.max(answer, dp[N-1][i]);
            }
            return answer;
        }


        solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]);
    }
    public int maxNumber(int a, int b, int c) {
        return Math.max(Math.max(a,b),c);
    }
}

