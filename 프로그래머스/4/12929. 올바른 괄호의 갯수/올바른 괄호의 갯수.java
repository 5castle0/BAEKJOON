class Solution {
    
    public int solution(int n) {
        return dfs(0,0,n);
    }
    
    private int dfs(int open, int close, int n){
         
        // 1. 닫힌 괄호가 더 많아지는 경우
        // 2. 열린 괄호가 n보다 커지는 경우
        if(open-close<0 || open>n){
            return 0;
        }
        
        if(open==close && open==n){
            return 1; 
        }    
        
        int ans = 0;
        
        ans += dfs(open+1, close, n);
        ans += dfs(open, close+1, n);
        
        return ans;
    }
}