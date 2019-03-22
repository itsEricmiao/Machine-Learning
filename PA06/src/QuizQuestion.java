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

    public void validateAnswer(String input)
    {
        if(input == answer)
        {
            System.out.println("True!");
        }else
        System.out.println("Wrong...");
    }

    public void display()
    {
        System.out.println(question);
    }

}
