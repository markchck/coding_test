import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
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

        
        // 뭐가 문제냐면?
        // 1번 도시에서 갈 수 있는 도시들을 큐에 넣을 때 [2, 2], [3, 3], [1, 4], [10, 5] 이렇게 넣고 우선 순위 큐로 가장 작은 비용의 값을 추출한다. 그럼 4번 도시가 추출이 되는데
        // 4번 도시와 인접한 도시를 추가할 때 만약 [3, 5] 이렇게 넣어 버리면 [2, 2], [3, 3], [3, 5], [10, 5] 이렇게 될 것이고
        // 따라서 1번 도시와 인접한 도시들과 4번 도시에서 인접한 도시 정보인 [3,5]가 섞여 버리는 문제가 발생 한다.
        // 그래서 1번 도시에서 인접한 도시들을 먼저 전부 방문하고 그 다음 4번 도시에서 인접한 도시를 방문하게 해야한다. (도시간 섞이지 않게 하는 방법이 필요 하다)
        // 결국 que에 nested하게 집어넣고 [[2, 2], [3, 3], [1, 4], [10, 5]] 이렇게 [2, 2], [3, 3], [1, 4], [10, 5] 이렇게 말고
        // que에서 팝을 한 뒤 [2, 2], [3, 3], [1, 4], [10, 5]를 cityInfoList 라고 하고
        // cityInfoList를 이터레이팅하여 nowCost, nowCity 라고 한다.


        // 만약 "result[nextCity]와  result[nowCity]  + nextCost" 중 작은 걸로 result[nowCity]를 갱신 해야 한다. //이 점화식을 만들어 줘야함.


        // 저 점화식을 어떻게 만들까?



        /**
        deque.append( [[2, 2], [3, 3], [1, 4], [10, 5]] )

        while (deque를)를 통해 deque를 인자가 있으면 반복하게 한다.
        deque를 popleft하고 cityInfos라고 함 (여러 도시들의 교통정보를 담고 있는 배열)
        cityInfos를 nowCost, nowCity로 이터레이팅 한다.

        if ( nowCity가 startCity이면) result[nowCity] 를 0으로 바꾼다. (result[startCity]는 자기 자신 이기 때문에 0으로 바꿔 줘야 함)
        다음 방문할 도시를 추가해야함.
        */



        /**
         *         que에 graph[startCity]를 하나씩 집어 넣는다. que = PriortyQue( [2, 2], [3, 3], [1, 4], [10, 5] )
         *
         *          while (que)를 통해 큐에 값이 있으면 반복 되게 한다.
         *              우선순위 큐의 pop을 활용해 가장 최소 비용 도시 부터 추출 하고 nowCost(=1) , nowCity(=4)라고 한다.
         *              현재의 result[nowCity]와 nowCost를 비교해서 작은 값으로 result[nowCity]를 갱신 한다.
         *              nowCity와 인접한 도시들을 큐에 넣는다. ( graph[nowCity]
         *
         *         ! 이렇게 하면 1번 도시가 갈 수 있는 도시와 4번도시가 갈 수 있는 도시가 큐에 섞이게 된다.
         */

    }
}