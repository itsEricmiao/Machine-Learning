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
        choice.addChoice(inputQuestion,false);


        System.out.println("Please enter your quiz choices to the question");
        for(int i = 0 ; i < 4; i++)
        {
            int counter = i+1;
            System.out.println(counter +":");
            String inputChoice = inputScan.nextLine();

            System.out.println("Is this the correct answer? (Y/N)");
            String ifAnswerStr = inputScan.nextLine();
            if(ifAnswerStr == "Y")
            {
                choice.addChoice(inputChoice, true);
            }else if(ifAnswerStr == "N")
            {
                choice.addChoice(inputChoice, false);
            }else
                {
                    System.out.print("Invalid input, please try again");
                }
        }

        choice.display();
        System.out.print("Your Answer: ");
        int userAnswer = inputScan.nextInt();
        System.out.println("Your choice is: "+userAnswer);
//        choice.validateAnswer(userAnswer);
    }
}
