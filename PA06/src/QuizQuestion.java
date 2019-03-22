public class QuizQuestion {
    private String question;
    private  String answer;

    public void QuizQuestion()
    {
        question = null;
        answer = null;

    }

    public void setQuestion(String inputStr)
    {
        question = inputStr;

    }

    public void setAnswer(String inputStr)
    {
        answer = inputStr;

    }

    boolean validateAnswer(String input)
    {
        if(input == answer)
        {
            return true;
        }
        return false;
    }

    public void display()
    {

    }

}
