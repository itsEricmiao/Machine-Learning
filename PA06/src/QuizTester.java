import java.util.Scanner;

public class QuizTester {

    static Scanner inputScan = new Scanner(System.in);
    public static void main(String[] args)
    {
        System.out.println("Welcome to Eric's Quiz app");
        ChoiceQuestion question = new ChoiceQuestion();
        presentQuestion(question);
    }

    public static void presentQuestion(ChoiceQuestion choice)
    {
        System.out.println("Please enter your quiz question description");
        String inputQuestion = inputScan.nextLine();
        choice.setQuestion(inputQuestion);

        for(int i = 0 ; i < 4; i++)
        {
            int counter = i+1;
            System.out.println("Please enter your quiz choices to the question");
            System.out.print(counter +":");
            String inputChoice = inputScan.nextLine();

            System.out.println("Is this the correct answer? (Type 1 as Yes and 2 as NO)");
            int ifAnswerStr = inputScan.nextInt();
            if(ifAnswerStr == 1)
            {
                choice.addChoice(inputChoice, true);
            }else if(ifAnswerStr == 2)
            {
                choice.addChoice(inputChoice, false);
            }else
                {
                    System.out.print("Invalid input, please try again");
                    break;
                }
            inputScan.nextLine();
        }

        choice.display();
        System.out.print("Your Answer: ");
        int userChoose = inputScan.nextInt();
        String userAnswer = choice.getChoice(userChoose-1);
        choice.validateAnswer(userAnswer);
    }
}
