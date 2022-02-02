import Head from 'next/head';
import styles from '../styles/Home.module.css';
import React from "react";

export default function Home() {
    const [keywordState, setKeywordState] = React.useState("");
    const [data, setData] = React.useState("");

    const getWeather = async (city) => {
        const weather = await fetch(`http://0.0.0.0:8000/v1/api/city_weather/?city=${city}`);  // just for demo, but not a best practice to use static url here
        if (weather.status === 200) {
            const response = await weather.json();
            setData(response);
        } else {
            setData("");
        }
    };

    const handleChange = (e) => {
        const value = e.target.value;
        setKeywordState(value);
        if(value.length > 0) {
            getWeather(value)
        }

    }

    return (
        <div className={styles.container}>
            <Head>
                <title>Search Weather</title>
            </Head>

            <main className={styles.main}>
                <h1 className={styles.title}>
                    Search Weather
                </h1>

                <p className={styles.description}>
                    <input className="input has-shadow is-medium is-rounded"
                           type="text"
                           placeholder="Search city ex: boston"
                           name="keyword"
                           onChange={handleChange}
                           value={keywordState}
                    />
                </p>

                <div className={styles.grid}>
                    <div className={styles.card}>
                        <h2>Current weather of  {keywordState}</h2>
                        <p>Current temperature: {data['current_temperature']} </p>
                        <p>Current air pressure: {data['current_pressure']}</p>
                        <p>Current air humidity: {data['current_humidity']}</p>
                    </div>
                </div>
            </main>
        </div>
    )
}
