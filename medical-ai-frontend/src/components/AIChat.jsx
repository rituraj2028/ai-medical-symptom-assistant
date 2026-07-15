import { useState} from "react";
import api from "../services/api";
import "./AIChat.css";

function AIChat({ disease }) {

    const [question, setQuestion] = useState("");
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);
    

    
    

    const askAI = async () => {

        if (!question.trim()) return;

        const userQuestion = question;

        setMessages(prev => [
            ...prev,
            {
                sender: "user",
                text: userQuestion
            }
        ]);

        setQuestion("");

        try {

            setLoading(true);

            const response = await api.post("/ask-ai", {
                disease,
                question: userQuestion
            });

            setMessages(prev => [
                ...prev,
                {
                    sender: "ai",
                    text: response.data.answer
                }
            ]);

        } catch (err) {

            setMessages(prev => [
                ...prev,
                {
                    sender: "ai",
                    text: "Sorry, I couldn't answer that question."
                }
            ]);

        } finally {

            setLoading(false);

        }

    };

    return (
        <div className="chat-card">

            <h2>🤖 Ask AI About This Disease</h2>

            <div className="messages">

                {messages.map((msg, index) => (

                    <div
                        key={index}
                        className={msg.sender}
                    >
                        <strong>
                            {msg.sender === "user" ? "You" : "AI"}
                        </strong>

                        <p>{msg.text}</p>

                    </div>

                ))}
                

            </div>

            <input
                value={question}
                onChange={(e)=>setQuestion(e.target.value)}
                placeholder="Ask a follow-up question..."
            />

            <button onClick={askAI}
            disabled={loading}
            >
                {loading ? "Thinking..." : "Ask AI"}
            </button>

            
            {messages.length > 0 && (
                <button className="clear-btn"
            onClick={()=> setMessages([])}>
                clear Chat
            </button>

            )}
            

        </div>
    );
}

export default AIChat;