import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import clsx from 'clsx';
import confetti from 'canvas-confetti';
import { useEffect, useRef, useState } from 'react';

// Typewriter Hook
const useTypewriter = (text: string, speed: number = 100) => {
  const [displayText, setDisplayText] = useState('');
  const [index, setIndex] = useState(0);

  useEffect(() => {
    if (index < text.length) {
      const timeout = setTimeout(() => {
        setDisplayText((prev) => prev + text.charAt(index));
        setIndex((prev) => prev + 1);
      }, speed);
      return () => clearTimeout(timeout);
    }
  }, [index, text, speed]);

  return displayText;
};

// Scroll Reveal Component
const FadeIn = ({ children, delay = 0 }: { children: React.ReactNode, delay?: number }) => {
  const [isVisible, setIsVisible] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
          observer.disconnect();
        }
      },
      { threshold: 0.1 }
    );
    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, []);

  return (
    <div
      ref={ref}
      className={`transition-all duration-1000 transform ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}
      style={{ transitionDelay: `${delay}ms` }}
    >
      {children}
    </div>
  );
};

import { Redirect } from '@docusaurus/router';
import { useAuth } from '../contexts/AuthContext';
import useBaseUrl from '@docusaurus/useBaseUrl';

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  const { user } = useAuth();
  const docsPath = useBaseUrl('/docs/module-1/intro-physical-ai-setup');

  if (user) {
    return <Redirect to={docsPath} />;
  }

  return (
    <header className="relative overflow-hidden min-h-[90vh] flex items-center justify-center bg-white dark:bg-[#0f172a] pb-24 pt-28">
      {/* Dynamic Background Elements */}
      <div className="absolute top-[-20%] right-[-10%] w-[800px] h-[800px] bg-indigo-500/10 rounded-full blur-[120px] animate-pulse" />
      <div className="absolute bottom-[-20%] left-[-10%] w-[600px] h-[600px] bg-purple-500/10 rounded-full blur-[100px] animate-bounce-slow" />

      <div className="container relative z-10 px-4">
        <div className="flex flex-col lg:flex-row items-center gap-12">

          {/* Left Content */}
          <div className="flex-1 text-center lg:text-left">
            <div className="inline-block px-4 py-1.5 mb-6 border border-indigo-500/30 rounded-full bg-indigo-500/10 backdrop-blur-sm">
              <span className="text-indigo-600 dark:text-indigo-300 font-semibold text-sm tracking-wide uppercase">
                The Future of Learning
              </span>
            </div>

            <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight mb-6 bg-clip-text text-transparent bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400 min-h-[1.2em]">
              {useTypewriter(siteConfig.title)}
              <span className="animate-pulse">|</span>
            </h1>

            <p className="text-xl md:text-2xl text-gray-600 dark:text-gray-300 mb-10 leading-relaxed">
              Master Physical-AI and Humanoid Robotics with an intelligent learning platform.
              Get personalized content, instant AI assistance, and hands-on knowledge.
            </p>

            <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start items-center">
              <Link
                className="button button--primary button--lg px-8 py-4 text-lg rounded-full shadow-lg hover:shadow-indigo-500/50 transition-all transform hover:-translate-y-1 relative overflow-hidden group"
                to="/signup"
                onMouseEnter={() => confetti({
                  particleCount: 100,
                  spread: 70,
                  origin: { y: 0.6 },
                  zIndex: 10000,
                })}
              >
                <span className="relative z-10">Get Started with Personalization</span>
                <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:animate-[shimmer_1.5s_infinite]" />
              </Link>
              <Link
                className="button button--lg px-8 py-4 text-lg rounded-full border-2 border-indigo-500/20 text-indigo-600 dark:text-indigo-300 hover:bg-indigo-50 dark:hover:bg-indigo-900/20 transition-all duration-300 font-semibold"
                to="/docs/module-1/intro-physical-ai-setup">
                Explore Content
              </Link>
            </div>
          </div>

          {/* Right Image */}
          <div className="flex-1 relative animate-fade-in mt-10 lg:mt-0">
            <div className="relative z-10 rounded-3xl overflow-hidden shadow-2xl border border-white/10 transform hover:scale-[1.02] transition-transform duration-500 max-w-lg mx-auto">
              <img
                src="img/hero_illustration.png"
                alt="Physical AI Illustration"
                className="w-full h-auto object-cover"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent pointer-events-none" />
            </div>
            {/* Floating Elements */}
            <div className="absolute -top-10 -right-10 w-24 h-24 bg-indigo-500 rounded-full blur-2xl opacity-30 animate-pulse" />
            <div className="absolute -bottom-10 -left-10 w-32 h-32 bg-purple-500 rounded-full blur-2xl opacity-30 animate-bounce-slow" />
          </div>
        </div>

        {/* Feature Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-32 text-left">
          <FadeIn delay={0}>
            <FeatureCard
              icon="🧠"
              title="Adaptive Learning"
              description="Content that adjusts to your expertise level, from Novice to Professional."
            />
          </FadeIn>
          <FadeIn delay={200}>
            <FeatureCard
              icon="💬"
              title="AI Tutor"
              description="Get instant answers from an AI assistant trained on the entire course curriculum."
            />
          </FadeIn>
          <FadeIn delay={400}>
            <FeatureCard
              icon="🌍"
              title="Bilingual Support"
              description="Seamlessly switch between English and Urdu to learn in your preferred language."
            />
          </FadeIn>
        </div>


      </div>
    </header>
  );
}

function FeatureCard({ icon, title, description }: { icon: string, title: string, description: string }) {
  return (
    <div className="p-8 rounded-2xl bg-white/50 dark:bg-white/5 border border-gray-200 dark:border-white/10 backdrop-blur-sm hover:bg-white/80 dark:hover:bg-white/10 transition-all duration-300 hover:shadow-2xl hover:-translate-y-2 group cursor-pointer hover:border-indigo-500/50 dark:hover:border-indigo-500/50 relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-br from-indigo-500/5 to-purple-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
      <div className="relative z-10">
        <div className="text-4xl mb-4 group-hover:scale-110 transition-transform duration-300">{icon}</div>
        <h3 className="text-xl font-bold mb-2 text-gray-900 dark:text-white">{title}</h3>
        <p className="text-gray-600 dark:text-gray-400 leading-relaxed">{description}</p>
      </div>
    </div>
  );
}

export default function Home(): JSX.Element {
  return (
    <Layout
      title="Home"
      description="AI-Native Textbook for Physical AI">
      <HomepageHeader />
    </Layout>
  );
}
