# Group-11: CSN341 Project Based on Emerging Protocols
In the dynamic realm of web technologies, emerging network protocols, notably exemplified by the Quick UDP Internet Connections (QUIC) protocol, promise to reshape application performance and user experience. This comprehensive problem statement explores the multifaceted challenges and 
opportunities inherent in analyzing the impact of these innovative protocols.

Web applications have become integral to modern online experiences, serving diverse users across varied devices and network conditions. Traditional protocols, such as 
Transmission Control Protocol (TCP) exhibits strengths but also limitations. Emerging alternatives like QUIC DoH and TLS offer transformative potential, sparking 
interest in their ability to revolutionize data transmission on the internet.

Understanding the implications of adopting emerging network protocols is crucial for stakeholders ranging from developers to end-users. The analysis is significant as 
it provides insights into potential benefits and challenges, influencing protocol adoption, infrastructure optimization, and user-centric design decisions.

The primary objectives of this research include evaluating how protocols like QUIC enhance web application performance and addressing issues like latency and head-of-
line blocking. Robust loss recovery mechanisms and their effectiveness in diverse network conditions are crucial considerations. The impact on the user experience, 
encompassing perceived speed and overall satisfaction, is a central focus. Additionally, the ability of protocols to facilitate seamless connection migration between 
different networks is examined, as is their standardization and compatibility with 
existing infrastructure.

The research methodology employs empirical studies, performance benchmarking, user surveys, and real-world simulations covering diverse 
scenarios. Anticipated outcomes extend beyond theoretical insights, aiming to provide practical information for web development, network optimization, and user 
experience design. The goal is to contribute to best practices for implementing emerging network protocols in diverse web environments, shaping a digital landscape 
that is both efficient and user-centric in the ever-evolving digital era.

## Analyzing the impact on web applications and user experience by following the protocols
## 1. QUIC
QUIC, or Quick UDP Internet Connections, is an experimental network protocol created by Google to minimize latency compared to TCP. 
LOW LATENCY: QUIC reduces latency for new connections to recently visited sites, eliminating head-of-line blocking in TLS and TCP. 
ENCRYPTION TRANSPORT: Encryption and privacy are fundamental to QUIC. Connections are protected from tampering and disruption, and most of the headers of the headers 
are not visible to third parties.
CONNECTION MIGRATION: QUIC addresses the "parking lot" issue through 18-byte connection IDs, enhancing loss recovery for connections in poor network conditions.

## 2. DoT(DNS over TLS)
DNS over TLS (DoT) encrypts DNS queries and responses using TLS, boosting user privacy and security by preventing eavesdropping. It operates on port 853, requiring support from both DNS clients and servers. Many popular web browsers, operating systems, and DNS services now embrace DoT for enhanced privacy and security.
BENEFITS:
- Encryption of DNS traffic
- Securing sensitive information
- Mitigating DNS spoofing and preventing DNS tampering
- Standardization and Interoperability
  
## 3. SCTP(Stream Control Transmission Protocol)
New applications are avoiding TCP due to issues like delays from head-of-line blocking, extra overhead in handling continuous data streams, and vulnerability to 
denial-of-service attacks like SYN attacks.

## 4. DoH(DNS over HTTPS)
DNS over HTTPS (DoH) encrypts DNS resolution using HTTPS, improving user privacy by concealing accessed websites from network observers, including ISPs.

IMPACT ON USER EXPERIENCE:
- Privacy and Security
- Control Over Online Experiences
- Minimal Impact on Web Browsing

## 5. TFO(TCP Fast Open)
TCP Fast Open (TFO) is a protocol extension that enables faster establishment of TCP connections by allowing data to be exchanged during the initial handshake, 
reducing latency in the communication process.

## 6. TLS 1.3
TLS 1.3 is the latest version of the Transport Layer Security (TLS) protocol, enhancing security and performance in communication over the internet by minimizing 
handshake complexity and improving encryption algorithms.
## 7. WebSocket Protocol
WebSocket is a communication protocol that provides full-duplex communication
channels over a single, long-lived connection, allowing for real-time data exchange between a client and a server in web applications.The advantage of WebSocket is that it enables real-time communication between the client and server without frequent HTTP requests/responses. This brings benefits such as reduced latency and improved performance and responsiveness of web apps. 

## 8. HTTP/3
HTTP/3 is an application layer protocol that utilizes the QUIC transfer protocol over UDP. It retains the familiar request-response model, status codes, and reliance 
on URLs seen in previous HTTP versions. Notably, HTTP/3 offers backward compatibility for a seamless transition in existing web infrastructure and introduces 
multiplexing to facilitate concurrent data transfers.

## 9. BBR
BBR is a congestion control algorithm by Google that enhances TCP performance. It optimizes data transmission by dynamically adjusting the sending rate based on the
characteristics of the network, aiming for high throughput and low latency. This is particularly beneficial for improving network performance in activities like web 
browsing and file transfers.

## 10. DRAP (A Proposed Protocol)
DRAP optimizes network performance through dynamic resource allocation, employing a specialized header for priority and efficient data transmission. It uses 
decentralized decision-making, adaptive algorithms, and security features like encryption. DRAP allows customization through QoS negotiation, includes congestion 
detection, and aims to balance adaptability and efficiency for enhanced network performance.

## Team Member
- [Shambhoolal Narwaria](https://github.com/mr-narwaria)
- [Abhishek Raj](https://github.com/Abhi9708bittu)
- [Sutirtha Ghosh](https://github.com/suti333)
- [Alhan Charan Beshra](https://github.com/ezio2605)
- [Sachin Jangid](https://github.com/sachin_jangid)
- [Ayushka Sahu](https://github.com/ayu-lif3)
- [Ganga Srujan](https://github.com/GangaSrujan)
- [Manoj Kumar Sial](https://github.com/manojkumar9911)
- [Chinchole Tushar Raju](https://github.com/chichole)
