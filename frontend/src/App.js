import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
    const [chats, setChats] = useState([]);
    const [messages, setMessages] = useState([]);
    const [currentChat, setCurrentChat] = useState(null);
    const [newMessage, setNewMessage] = useState('');
    const isAdmin = window.Telegram.WebApp.initDataUnsafe?.user?.id === 1271854660;

    useEffect(() => {
        if (isAdmin) {
            fetchChats();
        } else {
            fetchOrCreateUserChat();
        }
    }, []);

    const fetchChats = async () => {
        const response = await fetch('/api/chats');
        const data = await response.json();
        setChats(data);
    };

    const fetchOrCreateUserChat = async () => {
        const userId = window.Telegram.WebApp.initDataUnsafe?.user?.id;
        const response = await fetch(`/api/chats/${userId}`);
        const data = await response.json();
        setCurrentChat(data);
        fetchMessages(data.id);
    };

    const fetchMessages = async (chatId) => {
        const response = await fetch(`/api/messages/${chatId}`);
        const data = await response.json();
        setMessages(data);
    };

    const sendMessage = async () => {
        if (!newMessage.trim()) return;

        await fetch('/api/messages', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                chat_id: currentChat.id,
                sender_id: window.Telegram.WebApp.initDataUnsafe?.user?.id,
                content: newMessage
            })
        });

        setNewMessage('');
        fetchMessages(currentChat.id);
    };

    return (
        <div className="app">
            {isAdmin && (
                <div className="chats-list">
                    {chats.map(chat => (
                        <div
                            key={chat.id}
                            className="chat-item"
                            onClick={() => {
                                setCurrentChat(chat);
                                fetchMessages(chat.id);
                            }}
                        >
                            User ID: {chat.user_id}
                        </div>
                    ))}
                </div>
            )}

            <div className="chat-window">
                <div className="messages">
                    {messages.map(message => (
                        <div key={message.id} className={`message ${message.sender_id === window.Telegram.WebApp.initDataUnsafe?.user?.id ? 'sent' : 'received'}`}>
                            {message.content}
                        </div>
                    ))}
                </div>

                <div className="message-input">
                    <input
                        type="text"
                        value={newMessage}
                        onChange={(e) => setNewMessage(e.target.value)}
                        placeholder="Type a message..."
                    />
                    <button onClick={sendMessage}>Send</button>
                </div>
            </div>
        </div>
    );
}

export default App;
