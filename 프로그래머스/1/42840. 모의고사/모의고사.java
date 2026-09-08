class Solution {
    public int[] solution(int[] answers) {
        
        int[] person1 = {1, 2, 3, 4, 5};
        int[] person2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] person3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int[] correct = new int[3];
        
        // 맞은 개수 탐색
        for(int i=0; i<answers.length; i++){
            int answer = answers[i];
            
            if(person1[i%5]==answer) correct[0]++;
            if(person2[i%8]==answer) correct[1]++;
            if(person3[i%10]==answer) correct[2]++;
        }
        
        // 높은 점수 탐색
        int max = 0;
        int count = 0;
        
        for(int i=0; i<3; i++){
            if(correct[i] > max) {
                max = correct[i];
                count = 1;
            }else if(correct[i] == max){
                count++;
            }
        }
        
        // 높은 점수를 가진 사람 탐색
        int[] answer = new int[count];
        int idx = 0;
        for(int i=0; i<3; i++){
            if(correct[i] == max){
                answer[idx] = i+1;
                idx++;
            }
        }
        
        return answer;
    }
}