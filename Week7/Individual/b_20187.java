import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	  StringTokenizer s1 = new StringTokenizer(br.readLine());
	  int A = Integer.parseInt(s1.nextToken());
	  int N = (int) Math.pow(2,A);
	  int[][] arr = new int[N][N];
	  int check_LR = 0;
	  int check_TD = 0;
	  StringTokenizer s2 = new StringTokenizer(br.readLine());
	  for (int i = 0; i < A*2; i++) {
		
		  String k = s2.nextToken();
		  if (k.contains("L")) {
			  check_LR = 1;
		  }
		  else if (k.contains("R")){
			check_LR = -1;
		  }
		  else if (k.contains("D")){
			check_TD = -1;
		  }
		  else if (k.contains("U")){
			check_TD = 1;
		  }
		  
	  }
	  //종이의 1,1 부분의 방향 탐색
	  
	  StringTokenizer s3 = new StringTokenizer(br.readLine());
	  int B = Integer.parseInt(s3.nextToken());
	  int x = 0;
	  int y = 0;
	  int answer = 0; // 1,1의 무슨숫자가 들어갈지
	  if (B==0) {
		  x = -1;
		  y = 1;
	  }
	  else if(B==1) {
		  x = 1;
		  y = 1;
	  }
	  else if(B==2) {
		  x = -1;
		  y = -1;
	  }
	  else if(B==3) {
		  x = 1;
		  y = -1;
	  }
	  
	  x = x*check_LR;
	  y = y*check_TD;
	  
	  if (x==1 && y==1) {
		  answer = 1;
	  }
	  else if (x==1 && y==-1) {
		  answer = 3;
	  }
	  else if (x==-1 && y==-1) {
		  answer = 2;
	  }
	  else if (x==-1 && y==1) {
		  answer = 0;
	  }
	  
	  for (int i = 0; i < (int)N/2; i++) {
		  for (int l = 0; l < (int)N/2; l++) {
			  if (answer == 1) {
					arr[2*i][2*l] = 1;
					arr[2*i][2*l+1] = 0;
					arr[2*i+1][2*l] = 3;
					arr[2*i+1][2*l+1] = 2;
				}
			  else if (answer == 2) {
					arr[2*i][2*l] = 2;
					arr[2*i][2*l+1] = 3;
					arr[2*i+1][2*l] = 0;
					arr[2*i+1][2*l+1] = 1;
				}
			  else if (answer == 3) {
					arr[2*i][2*l] = 3;
					arr[2*i][2*l+1] = 2;
					arr[2*i+1][2*l] = 1;
					arr[2*i+1][2*l+1] = 0;
				}
			  else if (answer == 0) {
					arr[2*i][2*l] = 0;
					arr[2*i][2*l+1] = 1;
					arr[2*i+1][2*l] = 2;
					arr[2*i+1][2*l+1] = 3;
				}
		}
		
	  }
	  //반환된 answer는 0,0 배열의 점의 위치 나머지는 패턴에 따라 배열에 넣어주기만하면됨
	  
	  for (int i = 0; i < N; i++) {
		for (int k = 0; k < N; k++) {
			System.out.print(arr[i][k]);
			System.out.print(" ");
		}
		System.out.println("");
	}
  }
	

}