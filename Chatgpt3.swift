import OpenAI

let openAI = OpenAI(apiKey: "YOUR_API_KEY")

func sendMessage(message: String) {
  openAI.createCompletion(
    prompt: message,
    model: "text-davinci-002",
    temperature: 0.5,
    maxTokens: 128,
    topP: 1
  ) { result in
    switch result {
    case .success(let response):
      let chatbotResponse = response.text
      // Display the chatbot's response in the app
    case .failure(let error):
      print(error)
    }
  }
}
