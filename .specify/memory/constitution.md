# Project Constitution: Physical AI Learning Platform

## 1. Vision & Foundational Principles
**Project:** Interactive Physical AI & Robotics Education Platform
**Mission:** Build an intelligent, adaptive learning system where content dynamically responds to learners through personalization, multilingual support, and AI-powered assistance.

**Foundational Principles:**
1.  **Intelligence-First Design:** Content is interactive and context-aware, powered by retrieval-augmented generation for dynamic learning experiences.
2.  **Real-World Applicability:** Code examples and implementations must be production-ready and deployable to actual robotics hardware (Jetson platforms, robotic systems), ensuring practical relevance.
3.  **Universal Accessibility:** Educational content seamlessly switches between English and Urdu, making knowledge accessible across language barriers.
4.  **Technical Accuracy:** All technical specifications, API references, and physics concepts must be validated against authoritative sources and official documentation.

## 2. Quality Standards & Requirements

### A. Educational Content Standards
*   **Adaptive Complexity:** Beginner content maintains conceptual clarity suitable for introductory learners. Advanced content provides technical depth appropriate for engineering students.
*   **Learning Progression:** Content follows a structured flow: Conceptual Foundation → Mathematical Framework → Implementation Code → Practical Simulation.
*   **Visual Integrity:** All technical diagrams, flowcharts, and architecture visualizations must be code-generated using **Mermaid.js** to ensure accuracy and maintainability.
*   **Source Attribution:** Technical specifications and claims require proper citations following IEEE referencing standards.

### B. Technical Architecture Standards
*   **Content Format:** All educational material authored in **MDX** (Markdown with JSX) for Docusaurus framework integration.
*   **Interactive Components:**
    *   Core concepts require React-based interactive components (`<SimulationViewer />`, `<CodeBlock />`) rather than static HTML.
    *   Personalization layer (`<PersonalizationWrapper />`) must be integrated on all content pages for adaptive rendering.
*   **Backend Infrastructure:**
    *   RAG implementation uses **Qdrant** for vector embeddings and **Neon Postgres** for user session management.
    *   AI responses must stream progressively to minimize perceived latency.

### C. Multilingual & Accessibility Standards
*   **Translation Quality:** Urdu content must maintain technical precision with proper terminology (e.g., "Artificial Intelligence" → "Masnooi Zahanat"), managed through parallel MDX files or i18n configuration.
*   **Audio Integration:** Chapter summaries include high-quality text-to-speech audio overviews for enhanced accessibility.

## 3. Technical Constraints & Boundaries
*   **Deployment Target:** Platform must build and deploy successfully to **GitHub Pages** with static site generation.
*   **Platform Independence:** While examples may reference specific tools (NVIDIA Isaac Sim), core concepts must apply broadly to standard robotics frameworks (URDF, ROS 2).
*   **Security Requirements:** User preferences and authentication data must be protected through secure authentication mechanisms.

## 4. Validation Criteria
*   **Language Switching Performance:** Language toggle response time under 200ms for seamless user experience.
*   **AI Assistant Accuracy:** RAG chatbot provides contextually relevant answers with >90% accuracy for page-specific queries.
*   **Build Integrity:** Production build process (`npm run build`) completes without errors or broken link warnings.
*   **Feature Demonstration:** Core capabilities (personalization, multilingual support, AI assistance) clearly demonstrated within 60 seconds of platform interaction.