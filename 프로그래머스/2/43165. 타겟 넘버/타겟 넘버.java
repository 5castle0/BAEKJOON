import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        Queue<Point> q = new LinkedList();
        q.add(new Point(0,-1));
        
        while(!q.isEmpty()){
            Point now = q.remove();
            
            if(now.idx+1 == numbers.length){
                if(now.sum == target){
                    answer++;
                }
                
                continue;
            }
            
            q.add(new Point(now.sum + numbers[now.idx+1], now.idx+1));
            q.add(new Point(now.sum - numbers[now.idx+1], now.idx+1));
            
        }
        
        return answer;
    }
    
    class Point{
        int sum;
        int idx;
        
        Point(int sum, int idx){
            this.sum = sum;
            this.idx = idx;
        }
    }
}