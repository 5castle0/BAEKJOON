import java.util.*;

class Solution {
    public String solution(String X, String Y) {
        String answer = "";
        
        int[] count = new int[10];
        
        for(int i=0; i<X.length(); i++){
            int n = (int) X.charAt(i) - 48;
            
            count[n]++;
        }
        
        List<Integer> list = new ArrayList();
        for(int i=0; i<Y.length(); i++){
            int n = (int) Y.charAt(i) - 48;
            
            if(count[n] > 0){
                list.add(n);
                count[n]--;
            }
        }
        
        Collections.sort(list, Collections.reverseOrder());
        
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<list.size(); i++){
            sb.append(list.get(i));
        }
        
        answer = sb.toString();
        
        if(answer==""){
            return "-1";
        }
        
        if(answer.charAt(0)=='0'){
            return "0";
        }
       
        return answer;
    }
}