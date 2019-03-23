// CSE-3342 Spring 2019
// PA06: Inheritance
// Instructor: Nasser Jan
// Name: Eric Miao

import java.util.Scanner;

public class QuizTester {
    // Using a global Scanner object to get user inputs
    static Scanner inputScan = new Scanner(System.in);

    public static void main(String[] args)
    {
        System.out.println("Welcome to Eric's Quiz app\n");
            ChoiceQuestion question = new ChoiceQuestion();
            presentQuestion(question);
    }

    /*
        So this method is made of two parts:
        1. Asking user for question/answer input
        2. display question and ask for user's answer
    */
    public static void presentQuestion(ChoiceQuestion choice)
    {
        // Store Quiz description into the question string in QuizQuestion
        System.out.println("Please enter your quiz question: ");
        String inputQuestion = inputScan.nextLine();
        choice.setQuestion(inputQuestion);

        // Using a loop to store Quiz choices(1234) into the choices ArrayList in ChoiceQuestion
        for(int i = 0 ; i < 4; i++)
        {
            int counter = i+1;
            System.out.println("Please enter your quiz choices to the question");
            System.out.print(counter +":");
            String inputChoice = inputScan.nextLine();

            // Asking user if the input choice is the correct answer.
            // If YES, we store the choice into the choices ArrayList AND it will automatically pass this choice as the correct answer to QuizQuestion setAnswer().
            // If NOT, we simply store the choices into the choices ArrayList.
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

        // Below is the second part of the method which is display to question and ask for user input
        choice.display();
        System.out.print("Your Answer: ");
        int userChoose = inputScan.nextInt();
        // Getting the choice user chose from the arrayList and check if it is the correct answer.
        String userAnswer = choice.getChoice(userChoose-1);
        choice.validateAnswer(userAnswer);
    }
}
