class Solution {
    public String solution(int[] food) {
        String answer = "";
        
        for(int i=1; i<food.length; i++){
            int count = food[i]/2;
            
            for(int j=0; j<count; j++){
                answer += String.valueOf(i);
            }
        }
    
        String reverse = "";
        for(int i=answer.length()-1; i>=0; i--){
            reverse += answer.charAt(i);
        }
        
        answer += "0" + reverse;
        
        return answer;
    }
}