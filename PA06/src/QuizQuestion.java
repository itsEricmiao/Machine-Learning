public class QuizQuestion {
    private String question;
    private  String answer;

    /*
        Constructor for QuizQuestion
     */
    public void QuizQuestion()
    {
        question = null;
        answer = null;
    }

    /*
        Setter for question string
     */
    public void setQuestion(String inputStr)
    {
        question = inputStr;
    }

    /*
        Setter for answer string
     */
    public void setAnswer(String inputStr)
    {
        answer = inputStr;
    }

    /*
        Check if the user answer is correct
     */
    public void validateAnswer(String input)
    {
        if(input == answer)
        {
            System.out.println("True!");
        }else
        System.out.println("Wrong...");
    }

    /*
        Print out the question
     */
    public void display()
    {
        System.out.println(question);
    }

}
