import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        
        // skip할 문자들 배열
        int len = skip.length();
        char[] skipChar = new char[len];
        for(int i=0; i<len; i++){
            skipChar[i] = skip.charAt(i);
        }
        
        StringBuilder answer = new StringBuilder();
        for(int i=0; i<s.length(); i++){
            char now = s.charAt(i);
            
            int idx = index; // 이동할 거리
            
            for(int j=0; j<idx; j++){
                now++;
                
                if(now > 'z'){
                    now = 'a';
                }
                
                // now가 skip문자라면 한 번 더 이동
                for(char c : skipChar){
                    if(now==c) idx++;
                }
            }
            
            answer.append(now);
        }
        
        return answer.toString();
    }
}