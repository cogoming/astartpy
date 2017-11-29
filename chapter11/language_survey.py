from survey import  AnonymousSurvey
#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first lerrn to speak"
my_survey = AnonymousSurvey(question)
my_survey.show_question();
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language:")
    if response.lower() == 'q':
        break;
    my_survey.store_response(response);
my_survey.show_results()


