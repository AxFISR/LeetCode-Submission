class Solution {
    public boolean isValidSudoku(char[][] board) {
        
        //1. test rows
        for(int row = 0 ; row < 9 ; row++){
            int[] checker = new int[10];
            for(int idx = 0 ; idx < 9 ; idx++){
                if(board[row][idx] - '0' <= 9 && board[row][idx] - '0' >= 0){
                    checker[board[row][idx] - '0']++;
                    if(checker[board[row][idx] - '0'] > 1){
                        return false;
                    }
                }

            }
        }
        //2. test columns
        for(int column = 0 ; column < 9 ; column++){
            int[] checker = new int[10];
            for(int idx = 0 ; idx < 9 ; idx++){
                if(board[idx][column] - '0' <= 9 && board[idx][column] - '0' >= 0){
                    checker[board[idx][column] - '0']++;
                    if(checker[board[idx][column] - '0'] > 1){
                        return false;
                    }
                }
            }
        }

        //3. test boxes
        for(int i = 0 ; i < 9 ; i = i+3 ){
            for(int j = 0 ; j < 9 ; j = j+3){
                int[] checker = new int[10];
                for(int row = 0 ; row <3 ; row ++){
                    for(int col = 0 ; col < 3 ; col ++){
                        if(board[row+i][col+j] - '0' <= 9 && board[row+i][col+j] - '0' >= 0){
                            checker[board[row+i][col+j] - '0']++;
                            if(checker[board[row+i][col+j] - '0'] > 1){
                                return false;
                            }

                        }

                    }
                }
            }
        }

    return true;
    }

}