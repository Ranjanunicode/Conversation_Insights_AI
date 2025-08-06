# 🔎 API Usage and Sample Responses

## ✅ Get token
```bash
curl -X POST http://localhost:8000/auth/token -d "username=admin&password=admin123" -H "Content-Type: application/x-www-form-urlencoded"
```
### Sample Response
```bash
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc1NDQ1MzIwNn0.p1JAuilnaVYqsw33skEDWsyeSd7SiUFsnQXKOfyh8x8",
    "token_type": "bearer"
}
```

## ✅ Get All Calls
```bash
curl -H "Authorization: Bearer <your_jwt_token>" http://localhost:8000/api/v1/calls
```
### Sample Response
```bash
[
    {
        "call_id": "01e60c31-924d-4afc-a657-f81f5e4fc076",
        "agent_id": "75e46b82-d0ae-48ad-a245-ef0fe485b774",
        "customer_id": "e020713a-c822-4e6f-974d-e0c8a5e000f2",
        "language": "en",
        "start_time": "2025-04-26T07:02:47",
        "duration_seconds": 380,
        "transcript": "Agent: Hello, thank you for answering. My name is John, and I'm calling from XYZ Corporation. How are you today?\nCustomer: I'm doing well, thanks. Who is this again?\nAgent: I'm John from XYZ Corporation. We specialize in providing energy-efficient solutions for homes and businesses.\nCustomer: Okay, I think I've heard of you. What can you do for me?\nAgent: We've recently launched a new line of smart thermostats that can help reduce your energy bills by up to 30%.\nCustomer: That sounds interesting. I've been looking to upgrade my old thermostat.\nAgent: Great timing! Our smart thermostat is not only energy-efficient but also Wi-Fi enabled, allowing you to control it remotely.\nCustomer: That's a nice feature. How much does it cost?\nAgent: The price starts at $250, but we're currently offering a discount of $50 for first-time customers.\nCustomer: Okay, that's not bad. What kind of support do you offer?\nAgent: We provide 24/7 customer support and a 5-year warranty on all our products.\nCustomer: Alright, I think I'm interested. Can you tell me more about the installation process?\nAgent: Absolutely. We offer professional installation services, and it usually takes about an hour to complete.\nCustomer: Okay, that sounds good. Can you send me a quote and some more information?\nAgent: I'd be happy to. I'll send you an email with all the details. Would you like to schedule an installation appointment?\nCustomer: Yes, please. How soon can you schedule it?\nAgent: Let me check our calendar. (pause) How about next Wednesday?\nCustomer: That works for me. Thank you, John.\nAgent: You're welcome. I'll send you a confirmation email with all the details. Have a great day!",
        "agent_talk_ratio": 0.638,
        "customer_sentiment_score": 0.9994189739227295
    },
    ...
]
```

## ✅ Get One Call
```bash
curl -H "Authorization: Bearer <your_jwt_token>" http://localhost:8000/api/v1/calls/<call_id>
```
### Sample Response
```bash
{
    "call_id": "01e60c31-924d-4afc-a657-f81f5e4fc076",
    "agent_id": "75e46b82-d0ae-48ad-a245-ef0fe485b774",
    "customer_id": "e020713a-c822-4e6f-974d-e0c8a5e000f2",
    "language": "en",
    "start_time": "2025-04-26T07:02:47",
    "duration_seconds": 380,
    "transcript": "Agent: Hello, thank you for answering. My name is John, and I'm calling from XYZ Corporation. How are you today?\nCustomer: I'm doing well, thanks. Who is this again?\nAgent: I'm John from XYZ Corporation. We specialize in providing energy-efficient solutions for homes and businesses.\nCustomer: Okay, I think I've heard of you. What can you do for me?\nAgent: We've recently launched a new line of smart thermostats that can help reduce your energy bills by up to 30%.\nCustomer: That sounds interesting. I've been looking to upgrade my old thermostat.\nAgent: Great timing! Our smart thermostat is not only energy-efficient but also Wi-Fi enabled, allowing you to control it remotely.\nCustomer: That's a nice feature. How much does it cost?\nAgent: The price starts at $250, but we're currently offering a discount of $50 for first-time customers.\nCustomer: Okay, that's not bad. What kind of support do you offer?\nAgent: We provide 24/7 customer support and a 5-year warranty on all our products.\nCustomer: Alright, I think I'm interested. Can you tell me more about the installation process?\nAgent: Absolutely. We offer professional installation services, and it usually takes about an hour to complete.\nCustomer: Okay, that sounds good. Can you send me a quote and some more information?\nAgent: I'd be happy to. I'll send you an email with all the details. Would you like to schedule an installation appointment?\nCustomer: Yes, please. How soon can you schedule it?\nAgent: Let me check our calendar. (pause) How about next Wednesday?\nCustomer: That works for me. Thank you, John.\nAgent: You're welcome. I'll send you a confirmation email with all the details. Have a great day!",
    "agent_talk_ratio": 0.638,
    "customer_sentiment_score": 0.9994189739227295
}
```

## ✅ Get Recommendations for a Call
```bash
curl -H "Authorization: Bearer <your_jwt_token>" http://localhost:8000/api/v1/calls/<call_id>/recommendations
```
### Sample Response
```bash
{
    "recommendations": [
        {
            "call_id": "d22846be-d253-47d9-a974-36bb971133b1",
            "similarity": 0.916,
            "agent_id": "2e3d9499-ca01-47a6-a183-3a9bcc024577",
            "start_time": "2025-05-11T04:45:33",
            "sentiment": 0.9994189739227295
        },
        {
            "call_id": "a108e4a6-7870-4e2c-90a6-5c6cba20a580",
            "similarity": 0.914,
            "agent_id": "4b58b5ca-73fe-4005-ae82-572797d9e4a5",
            "start_time": "2025-01-18T20:12:22",
            "sentiment": 0.9936303496360779
        },
        {
            "call_id": "9e36c07b-57e2-4445-af58-c24d57396480",
            "similarity": 0.911,
            "agent_id": "08347085-531a-48e3-a318-6569bacc269d",
            "start_time": "2025-05-15T22:30:13",
            "sentiment": 0.9974737763404846
        },
        {
            "call_id": "6b79c04b-4f06-499a-bbab-5c9b22a80eed",
            "similarity": 0.908,
            "agent_id": "71d32a33-fd99-442c-a150-4266f7339b63",
            "start_time": "2025-05-11T01:14:33",
            "sentiment": 0.9966394901275635
        },
        {
            "call_id": "6a9dfe52-c6b2-4fa9-8634-c708ff1f357e",
            "similarity": 0.906,
            "agent_id": "57e07b5f-7927-4594-ad47-dd162d205eeb",
            "start_time": "2025-04-13T20:45:48",
            "sentiment": 0.9975131750106812
        }
    ],
    "nudges": [
        "Try letting the customer talk more.",
        "Use positive reinforcement when customer hesitates.",
        "Summarize benefits clearly after listing features."
    ]
}
```

## ✅ Get Agent Leaderboard
```bash
curl -H "Authorization: Bearer <your_jwt_token>" http://localhost:8000/api/v1/analytics/agents
```
### Sample Response
```bash
[
    {
        "agent_id": "00e0aa9e-fac4-434f-a355-fd83c934875f",
        "total_calls": 1,
        "avg_sentiment": 1.0,
        "avg_talk_ratio": 0.69
    },
    ...
]
```

## ✅ Get Realtime Sentiment analysis using Websocket
```bash
wscat -c ws://localhost:8000/ws/sentiment
```