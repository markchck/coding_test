import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class 최소비용구하기_다익스트라 {
    public static void main(String[] args) {
        //dfs, bfs, dp, 다익스트라, 플루이드워셜, 이진탐색, 백트래킹, 스택
        //시간이 0.5초로 매우 타이트함(완전 탐색류 제외) bfs, dfs(백트래킹), dp(플루이드워셜) / 1000 * 100000 = 1억 (1초 예상됨)
        //시간이 부족하므로 필요한 도시만 가 봐야함 (따라서 다익스트라)

        Scanner sc = new Scanner(System.in);

        // N = 도시의 개수 입력
        String n = sc.nextLine();
        Integer N = Integer.parseInt(n);


        // M = 버스의 개수 입력
        Integer M =sc.nextInt();

        // 그래프 입력 받기
        ArrayList<ArrayList<int[]>> graph = new ArrayList<>(N+1);

        for (int i=0; i<N+1; i++){
            graph.add(new ArrayList<>());
        }

        // graph = [ [], [[2, 2], [3, 3], [1, 4], [10, 5]] , [[2, 4]] , [[1, 4], [1, 5]], [[3, 5]] ] 과 같은 형태로 입력 받음 // 최솟값을 추출 해야 하니 버스 비용을 앞에 두겠음. [비용, 도시] 순서

        for (int i =0 ; i < M; i++){
            int start = sc.nextInt();
            int end = sc.nextInt();
            int cost = sc.nextInt();
            graph.get(start).add(new int[] {end, cost});
        }

        // startCity = 출발 도시 입력 (예시 1번 도시)
        int startCity = sc.nextInt();

        // endCity = 도착 도시 입력 (예시 5번 도시)
        int endCity = sc.nextInt();


        // 1번 도시가 각 도시를 방문 하는 최솟값을 기록할 정답 배열 생성 (더 저렴한 경로를 찾으면 갱신할 것 이기에 매우 큰 값으로 초기화)
        int[] result = new int[N + 1];
        Arrays.fill(result, Integer.MAX_VALUE);

        // result = [ INF, 0, INF, INF, INF, INF]
        result[startCity] = 0;

        // deque( [0, 1] )

        PriorityQueue< int[] > que = new PriorityQueue<>((a,b)->a[1]-b[1]); // 2번째 인자를 기준으로 큐를 돌리고 싶으면?
        que.add(new int [] {startCity, 0});

        // while (deque)를 통해 deque를 인자가 있으면 반복 하게 한다.
        while(!que.isEmpty()){
            // que에서 최소를 뽑고 nowCost, nowCity라고 한다.
            int[] info = que.poll(); //
            int nowCity = info[0];
            int nowCost = info[1];

            // 만약 nowCost가 result[nowCity] 보다 크면 continue
            if (nowCost > result[nowCity]){
                continue;
            }else{
                //graph[nowCity]를  이터레이팅 돈다. (nextCost, nextCity)
                for(int i =0; i < graph.get(nowCity).size(); i++){
                    int newCity = graph.get(nowCity).get(i)[0];
                    int newCost = graph.get(nowCity).get(i)[1];

                    // if result[nextCity] > result[nowCity]  + nextCost 이면
                    if(result[newCity] > result[nowCity] + newCost){
                        // result[nextCity] = result[nowCity]  + nextCost
                        result[newCity] = result[nowCity] + newCost;

                        // que.append([nextCost, nextCity])
                        que.add( new int[] {newCity,newCost});
                    }

                }

            }
        }
        // result[endCity]출력하면 끝
        System.out.println(result[endCity]);
        sc.close();



    }
}
