import java.util.ArrayList;
public class ChoiceQuestion extends QuizQuestion {
private ArrayList<String> choices = new ArrayList<String>();

    /*
        AddChoice will store inputChoice string into the ArrayList
        If the inputChoice is the correct answer, it will pass this string into setAnswer() in parent Class.
     */
    public void addChoice(String inputChoice, boolean correct)
    {
        if(correct == false)
        {
            choices.add(inputChoice);
        }else if(correct == true)
        {
            choices.add(inputChoice);
            super.setAnswer(inputChoice);
        }
    }

    /*
        This is the display function that will display the parent Class's display()
        And using loop to display the choices.
     */
    public void display()
    {
        super.display();
        for(int i = 0; i < choices.size(); i++)
        {
            int counter = i+1;
            System.out.println(counter + ": " + choices.get(i));
        }
    }

    /*
        This is the getter for ArrayList choices
     */
    public String getChoice(int index)
    {
        return choices.get(index);
    }
}
