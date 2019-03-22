import java.util.ArrayList;
public class ChoiceQuestion extends QuizQuestion {
private ArrayList<String> choices = new ArrayList<String>();

//    public void ChoiceQuestion()
//    {
//        choices = ;
//    }

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

    public void display()
    {
        super.display();
        for(int i = 0; i < choices.size(); i++)
        {
            int counter = i+1;
            System.out.println(counter + ": " + choices.get(i));
        }
    }

    public String getChoice(int index)
    {
        return choices.get(index);
    }
}
