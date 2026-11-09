# 자연의 언어로 과학 읽기: 교과서 문장의 미분 방정식 번역과 다원 동역학계

> *"자연이라는 거대한 책은 수학이라는 언어로 쓰여 있다." - 갈릴레오 갈릴레이*
> 
> 고등학교 수학에서 배우는 도함수와 적분은 단순한 문제 풀이용 계산 기법이 아니라, 자연의 변화를 정량적으로 관찰하고 서술하기 위해 창안된 '자연의 언어'입니다.  
> 본 문서는 **과학 교과서의 실제 서술 문장을 단어 단위로 분해하여 미분 방정식 기호로 1:1 번역하는 스캐폴딩(Scaffolding)**에서 출발합니다. 이를 통해 미분형 단위($\frac{[y]}{[x]}$)와 적분형 단위($[y] \times [x]$)의 쌍대성을 검증하고, 나아가 2원 연립 피식-포식 모델과 감염병 SIR $\to$ SIRD 모델까지 자연의 상호작용을 수학으로 직관화하는 통합 탐구 아카이브입니다.

---

## Step 0. 자연어 $\leftrightarrow$ 수학 기호 '번역(Formulation)' 및 '차원 대칭성' 사전

### 1. 교과서 문장 분해 6대 번역 규칙

| 교과서 문장 표현 (자연어)                  | 수학적 의미                | 변환 기호 및 대수식                                                            |
|:-------------------------------- |:--------------------- |:----------------------------------------------------------------------:|
| **"시간 $t$에 따른 물리량 $A$의 변화율"**    | 순간 변화율 (시간에 대한 도함수)   | $\displaystyle \frac{dA}{dt}$                                          |
| **"깊이 $z$에 따른 물리량 $T$의 변화율"**    | 공간 구배 (공간 좌표에 대한 도함수) | $\displaystyle \frac{dT}{dz}$                                          |
| **"$A$의 변화율은 $B$에 비례한다"**        | 변화율과 대상 간의 선형 비례 관계   | $\displaystyle \frac{dA}{dt} \propto B \implies \frac{dA}{dt} = k B$   |
| **"두 집단 $A, B$ 사이의 접촉 / 만남 빈도"** | 확률적 조우 (질량 작용의 법칙)    | $A \times B$ ($AB$의 곱 형태)                                              |
| **"변화를 방해함 / 소모되어 감소함 / 기아 사망"** | 평형 유지 인과율 및 감소 추세     | $-$ (음의 부호)                                                            |
| **"전체 인구 / 에너지가 일정하게 보존됨"**      | 계 전체 합의 불변 (닫힌 상태계)   | $\displaystyle \sum \frac{dX_i}{dt} = 0 \implies \sum X_i = \text{상수}$ |

---

### 2. 수식 검증의 나침반: 미분형 단위와 적분형 단위의 쌍대성 (Duality)

| 연산 구분      | 기하학적 / 물리적 본질                  | 극한 정의                                                           | 단위(차원) 연산 규칙                                                 | 대표 물리 예시 (역학)                                                                                                         |
|:---------- |:------------------------------ |:---------------------------------------------------------------:|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------- |
| **미분형 단위** | **국소적 순간 변화율** (나눗셈, Rate)     | $\displaystyle \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}$ | $\displaystyle \left[\frac{dy}{dx}\right] = \frac{[y]}{[x]}$ | $\displaystyle \left[\frac{dv}{dt}\right] = \frac{[v]}{[t]} = \frac{\mathrm{m/s}}{\mathrm{s}} = \mathrm{m/s^2} = [a]$ |
| **적분형 단위** | **거시적 누적량** (곱셈, Accumulation) | $\displaystyle \lim_{\Delta x \to 0} \sum y \Delta x$           | $\displaystyle \left[\int y\,dx\right] = [y] \times [x]$     | $\displaystyle \left[\int a\,dt\right] = [a] \times [t] = (\mathrm{m/s^2}) \times \mathrm{s} = \mathrm{m/s} = [v]$    |

---

## Step 1. [물리학] 역학과 장(Field)의 동태성 모델링

### 📍 [탐구 1-1] 뉴턴 운동 법칙: 서술 문장에서 미분 방정식 조립하기

* **교과서 원문**: 
  
  > *"속도는 시간에 따른 위치의 변화율이며, 가속도는 시간에 따른 속도의 변화율이다. 물체의 가속도는 작용하는 알짜힘에 비례하고 질량에 반비례한다. 가속도-시간 그래프 밑넓이는 속도 변화량, 속도-시간 그래프 밑넓이는 변위이다."*

**[문항 1-1-1: 교과서 문장 1:1 분해 번역]**  
위 교과서 문장을 쉼표 단위로 쪼개어 각각 수학 기호로 번역해 보시오.

1. "속도는 시간에 따른 위치($x$)의 변화율이다" $\implies v(t) =$ ( $\qquad$ )
2. "가속도는 시간에 따른 속도($v$)의 변화율이다" $\implies a(t) =$ ( $\qquad$ )
3. "가속도는 알짜힘($F$)에 비례하고 질량($m$)에 반비례한다" $\implies a =$ ( $\qquad$ )
4. 1~3번을 결합하여 힘 $F$와 위치 $x$ 사이의 **2계 상미분 방정식**을 완성하시오: $F =$ ( $\qquad$ )

**[문항 1-1-2: 미분형·적분형 단위 검증]**  
미분형 단위 규칙($\left[\frac{dy}{dx}\right] = \frac{[y]}{[x]}$)과 적분형 단위 규칙($\left[\int y\,dx\right] = [y][x]$)을 적용하여, 가속도 단위 유도 및 정적분을 통한 속도 단위 복원 과정을 증명하시오.

**[문항 1-1-3: 누적의 적분형 수식화]**  
시간 구간 $[t_1, t_2]$ 동안 '그래프 밑넓이'를 정적분 기호로 표현하여 속도 변화량($\Delta v$)과 변위($\Delta x$)를 나타내시오.

<details class="insight-box">
<summary style="cursor: pointer; font-weight: bold; color: #0366d6; margin-top: 10px;">💡 [탐구 1-1] 문장 수식화 단계별 해설 및 차원 분석 보기 (클릭)</summary>
<div style="background-color: #f6f8fa; padding: 16px; border-left: 4px solid #0366d6; margin-top: 10px; border-radius: 4px;">

* **1단계: 자연어 $\to$ 수식 분해 번역 과정**:
  
  1. "시간 $t$에 따른 위치 $x$의 변화율" $\implies v(t) = \frac{dx}{dt}$
  2. "시간 $t$에 따른 속도 $v$의 변화율" $\implies a(t) = \frac{dv}{dt} = \frac{d}{dt}\left(\frac{dx}{dt}\right) = \frac{d^2x}{dt^2}$
  3. "알짜힘 $F$에 비례($\propto F$)하고 질량 $m$에 반비례($\propto \frac{1}{m}$)" $\implies a = \frac{F}{m} \iff F = ma$
  4. **방정식 최종 조립**: $F = m\frac{dv}{dt} = m\frac{d^2x}{dt^2}$

* **2단계: 단위의 쌍대성(Duality) 검증**:
  
  * $[x] = \mathrm{m}, \quad [t] = \mathrm{s}$
  * **미분형 단위**: $[v] = \left[\frac{dx}{dt}\right] = \frac{[x]}{[t]} = \mathrm{m/s}$
  * **미분형 단위**: $[a] = \left[\frac{dv}{dt}\right] = \frac{[v]}{[t]} = \frac{\mathrm{m/s}}{\mathrm{s}} = \mathrm{m/s^2}$
  * **적분형 단위**: $\left[\int a\,dt\right] = [a] \times [t] = (\mathrm{m/s^2}) \times \mathrm{s} = \mathrm{m/s} = [v]$ (속도 차원 완벽 복원)
  * 알짜힘 단위: $[F] = [m][a] = \mathrm{kg \cdot m/s^2} = \mathrm{N}$ (뉴턴)

* **3단계: 적분형 누적 모델**:
  $$ \Delta v = v(t_2) - v(t_1) = \int_{t_1}^{t_2} a(t) \, dt, \quad \Delta x = x(t_2) - x(t_1) = \int_{t_1}^{t_2} v(t) \, dt $$

* **교수학습 인사이트**: 뉴턴은 힘을 '속도'의 원인이 아니라 **'속도의 시간당 변화율(가속도)'을 일으키는 원인**으로 정의했습니다. 이 문장을 수식화한 결과가 바로 고전 역학을 지배하는 2계 미분 방정식 $F = m\frac{d^2x}{dt^2}$입니다.

</div>
</details>

---

### 📍 [탐구 1-2] 패러데이 전자기 유도 법칙: '방해'의 부호화

* **교과서 원문**: 
  
  > *"임의의 폐회로에서 발생하는 유도 기전력($\mathcal{E}$)의 크기는 폐회로를 통과하는 자기선속($\Phi_B$)의 시간에 따른 변화율과 같다. 유도 기전력은 자기선속의 변화를 방해하는 방향으로 유도되며, 코일의 감은 수($N$)에 비례한다."*

**[문항 1-2-1: 단어 대 단어 수식 분해]**

1. "자기선속($\Phi_B$)의 시간에 따른 변화율" $\implies$ 기호: ( $\qquad$ )
2. "변화를 방해하는 방향 (렌츠의 법칙)" $\implies$ 부호: ( $\qquad$ )
3. "코일 감은 수 $N$에 정비례" $\implies$ 비례계수: ( $\qquad$ )
4. 조각들을 결합하여 유도 기전력 $\mathcal{E}$의 미분 방정식을 완성하시오: $\mathcal{E} =$ ( $\qquad$ )

**[문항 1-2-2: 미분형 단위 유도]**  
자기선속의 단위가 웨버($\mathrm{Wb} = \mathrm{V \cdot s}$)일 때, $\left[\frac{d\Phi_B}{dt}\right]$의 미분형 단위 연산을 통해 기전력의 단위가 볼트($\mathrm{V}$)가 됨을 증명하시오.

<details class="insight-box">
<summary style="cursor: pointer; font-weight: bold; color: #0366d6; margin-top: 10px;">💡 [탐구 1-2] 문장 수식화 단계별 해설 및 차원 분석 보기 (클릭)</summary>
<div style="background-color: #f6f8fa; padding: 16px; border-left: 4px solid #0366d6; margin-top: 10px; border-radius: 4px;">

* **1단계: 자연어 $\to$ 수식 번역 과정**:
  
  * "시간에 따른 자기선속의 변화율" $\implies \frac{d\Phi_B}{dt}$
  * "변화를 방해하는 방향" $\implies -$ (음의 부호)
  * "감은 수 $N$에 비례" $\implies \times N$ (단, 감은 수는 단위가 없는 순수 정수)
  * **수식 완성**: $\mathcal{E} = -N \frac{d\Phi_B}{dt}$

* **2단계: 미분형 단위 검증**:
  $$ [\mathcal{E}] = \left[\frac{d\Phi_B}{dt}\right] = \frac{[\Phi_B]}{[t]} = \frac{\mathrm{V \cdot s}}{\mathrm{s}} = \mathrm{V} \quad (\text{기전력 단위 볼트 성립}) $$

* **3단계: 물리적 통찰 (부호의 의미)**:
  음의 부호($-$)는 시스템의 자생적 복원력이자 **에너지 보존 법칙**의 수식적 반영입니다. 만약 부호가 $+$라면 자속의 증가가 더 큰 전류를 만들고, 이 전류가 다시 자속을 폭주시키는 영구기관이 발생합니다.

</div>
</details>

---

### 📍 [탐구 1-3] 뉴턴의 냉각 법칙: 온도 차이와 평형 수렴의 수식화

* **교과서 원문**: 
  
  > *"뜨거운 커피는 주변 공기와의 온도 차이가 클수록 더 빠르게 식는다. 즉, 물체의 온도 변화율은 물체의 온도($T$)와 주변 환경 온도($T_{\text{env}}$)의 차이에 비례한다."*

**[문항 1-3-1: 문장 분해를 통한 미분 방정식 조립]**

1. "시간에 따른 물체의 온도($T$) 변화율" $\implies$ ( $\qquad$ )
2. "물체의 온도($T$)와 환경 온도($T_{\text{env}}$)의 차이" $\implies$ ( $\qquad$ )
3. "온도가 식는다 (환경 온도로 감소 수렴)" $\implies$ 부호: ( $\qquad$ )
4. 비례상수 $k > 0$를 결합하여 미분 방정식을 완성하시오: $\frac{dT}{dt} =$ ( $\qquad$ )

**[문항 1-3-2: 차원 분석과 무차원 지수]**  
미분형 단위 연산을 통해 비례상수 $k$의 단위를 구하고, 지수 해 $e^{-kt}$에서 왜 지수부 $kt$가 무차원이어야 하는지 서술하시오.

**[문항 1-3-3: 변수 분리를 통한 적분형 구성]**  
온도 변수 $T$와 시간 변수 $t$를 분리하여 적분형 방정식을 구성하시오.

<details class="insight-box">
<summary style="cursor: pointer; font-weight: bold; color: #0366d6; margin-top: 10px;">💡 [탐구 1-3] 문장 수식화 단계별 해설 및 차원 분석 보기 (클릭)</summary>
<div style="background-color: #f6f8fa; padding: 16px; border-left: 4px solid #0366d6; margin-top: 10px; border-radius: 4px;">

* **1단계: 자연어 $\to$ 수식 번역 과정**:
  
  * "온도의 시간 변화율" $\implies \frac{dT}{dt}$
  * "온도 차이" $\implies (T - T_{\text{env}})$
  * "뜨거운 물체($T > T_{\text{env}}$)는 식어야 하므로($\frac{dT}{dt} < 0$)" $\implies$ 음의 부호 $-$
  * "비례한다" $\implies$ 비례상수 $k$ 결합
  * **최종 미분 방정식**: $\frac{dT}{dt} = -k(T - T_{\text{env}})$

* **2단계: 미분형 단위 및 무차원성 분석**:
  
  * 좌변: $\left[\frac{dT}{dt}\right] = \frac{[T]}{[t]} = \frac{\mathrm{K}}{\mathrm{s}}$
  * 우변: $[T - T_{\text{env}}] = \mathrm{K}$
  * 등호 성립: $\frac{\mathrm{K}}{\mathrm{s}} = [k] \times \mathrm{K} \implies [k] = \mathrm{s^{-1}} = \frac{1}{\mathrm{s}}$
  * 지수항의 무차원성: $[kt] = [k] \times [t] = \mathrm{s^{-1}} \times \mathrm{s} = 1$ (단위 없는 순수한 실수)

* **3단계: 변수 분리 적분형**:
  $$ \int \frac{1}{T - T_{\text{env}}} \, dT = \int -k \, dt \implies T(t) = T_{\text{env}} + (T_0 - T_{\text{env}})e^{-kt} $$

</div>
</details>

---

## Step 2. [화학] 반응 속도론과 농도 의존성의 해석

### 📍 [탐구 2-1] 화학 반응 속도식: '감소율'의 부호와 반응 차수

* **교과서 원문**: 
  
  > *"화학 반응의 속도($v$)는 시간에 따른 반응물 농도($[A]$)의 감소율로 정의된다. 1차 반응에서 반응 속도는 반응물의 현재 농도에 정비례하며, 비례상수를 반응 속도 상수($k$)라고 한다."*

**[문항 2-1-1: 교과서 정의의 수식화]**

1. "시간에 따른 반응물 농도 $[A]$의 변화율" $\implies$ ( $\qquad$ )
2. "반응물이 소모되어 감소하는 속도이므로 양수로 정의함" $\implies v = -$ ( $\qquad$ )
3. "반응물 농도 $[A]$의 1제곱에 비례함" $\implies v = k \times$ ( $\qquad$ )
4. 두 식을 연결하여 1차 미분 속도식을 완성하시오: $-\frac{d[A]}{dt} =$ ( $\qquad$ )

**[문항 2-1-2: 반응 차수별 $k$의 미분형 단위 유도]**  
농도 단위 $\mathrm{M} = \mathrm{mol/L}$, 시간 단위 $\mathrm{s}$일 때:

* 반응 속도 $v = -\frac{d[A]}{dt}$의 미분형 단위: $[v] =$ ( $\qquad$ )
* 1차 반응($v = k[A]$)의 속도상수 단위: $[k] =$ ( $\qquad$ )
* 2차 반응($v = k[A]^2$)의 속도상수 단위: $[k] =$ ( $\qquad$ )

**[문항 2-1-3: 반감기 공식과 농도 독립성의 증명]**  
적분 속도식 $\int_{[A]_0}^{[A]_t} \frac{1}{[A]} \, d[A] = \int_0^t -k \, dt$를 풀어 $[A]_t = [A]_0 e^{-kt}$를 유도하고, 반감기 $t_{1/2} = \frac{\ln 2}{k}$에서 왜 초기 농도 $[A]_0$가 완전히 소거되는지 설명하시오.

<details class="insight-box">
<summary style="cursor: pointer; font-weight: bold; color: #0366d6; margin-top: 10px;">💡 [탐구 2-1] 문장 수식화 단계별 해설 및 차원 분석 보기 (클릭)</summary>
<div style="background-color: #f6f8fa; padding: 16px; border-left: 4px solid #0366d6; margin-top: 10px; border-radius: 4px;">

* **1단계: 자연어 $\to$ 수식 번역 과정**:
  
  * "농도의 시간 변화율" $\implies \frac{d[A]}{dt}$
  * 반응물은 시간이 갈수록 줄어들므로 도함수 $\frac{d[A]}{dt} < 0$입니다. 화학자들은 '속도'를 항상 양수로 다루기 위해 앞에 음의 부호를 붙입니다 $\implies v = -\frac{d[A]}{dt}$
  * "농도에 정비례" $\implies v = k[A]$
  * **최종 미분 속도식**: $-\frac{d[A]}{dt} = k[A]$

* **2단계: 반응 차수별 미분형 단위 유도**:
  
  * $[v] = \left[\frac{d[A]}{dt}\right] = \frac{[[A]]}{[t]} = \frac{\mathrm{M}}{\mathrm{s}} = \mathrm{mol \cdot L^{-1} \cdot s^{-1}}$
  * **1차 반응**: $\frac{\mathrm{M}}{\mathrm{s}} = [k] \times \mathrm{M} \implies [k] = \mathrm{s^{-1}}$
  * **2차 반응**: $\frac{\mathrm{M}}{\mathrm{s}} = [k] \times \mathrm{M^2} \implies [k] = \mathrm{M^{-1}\cdot s^{-1}} = \mathrm{L \cdot mol^{-1} \cdot s^{-1}}$

* **3단계: 반감기 수학적 증명**:
  $$ \ln\frac{[A]_t}{[A]_0} = -kt \implies \text{반감기 조건 } [A]_t = \frac{1}{2}[A]_0 \text{ 대입} \implies \ln\left(\frac{1}{2}\right) = -kt_{1/2} $$
  $$ t_{1/2} = \frac{\ln 2}{k} \approx \frac{0.693}{k} $$
  *로그 내부에서 농도 단위가 약분($\mathrm{M}/\mathrm{M} = 1$)되어 무차원이 되기 때문에*, **1차 반응의 반감기는 출발 농도에 전혀 영향을 받지 않습니다.**

</div>
</details>

---

## Step 3. [생명과학 & 역학] 개체군 동태학과 상호작용 네트워크

### 📍 [탐구 3-1] J자형 및 S자형(로지스틱) 생장 모델: '환경 저항'의 수식화

* **교과서 원문**: 
  
  > *"자원이 무제한인 이상적 환경에서 개체군의 개체 수($N$) 증가는 개체들의 번식에 비례하여 기하급수적으로 증가한다(J자형). 그러나 실제 환경에서는 개체 수가 증가함에 따라 먹이 부족, 서식지 경쟁 등의 환경 저항이 커져 생장 속도가 둔화되며, 환경 수용 능력($K$)에 도달하면 개체 수는 더 이상 증가하지 않고 일정하게 유지된다(S자형)."*

**[문항 3-1-1: 이상적 환경 (J자형) 번역]**

1. "시간에 따른 개체 수($N$)의 증가율" $\implies$ ( $\qquad$ )
2. "현재 존재하는 개체 수($N$) 자체에 비례 (개체가 많을수록 출생자도 많음)" $\implies$ 비례상수 $r$ 도입
3. 미분 방정식 완성: $\frac{dN}{dt} =$ ( $\qquad$ )

**[문항 3-1-2: 환경 저항 (S자형 로지스틱) 인자 조립]**

1. "개체 수 $N$이 증가할수록 성장을 방해하여 $0$으로 수렴시키는 억제 인자":
   * $N \ll K$일 때 $\approx 1$ (영향 없음)
   * $N \to K$일 때 $\to 0$ (성장 완전 멈춤)
   * 위 조건을 만족하는 가장 단순한 1차 분수 인자는? $\implies$ ( $\qquad$ )
2. J자형 모델에 환경 저항 인자를 곱하여 **로지스틱 미분 방정식**을 완성하시오: $\frac{dN}{dt} =$ ( $\qquad$ )

**[문항 3-1-3: 단위 검증]**  
개체 수 $N$($\text{마리}$), 시간 $t$($\text{일}$)일 때, $\frac{dN}{dt}$의 미분형 단위와 내적 자연 증가율 $r$, 환경 수용 능력 $K$의 단위를 각각 구하시오.

<details class="insight-box">
<summary style="cursor: pointer; font-weight: bold; color: #0366d6; margin-top: 10px;">💡 [탐구 3-1] 문장 수식화 단계별 해설 및 차원 분석 보기 (클릭)</summary>
<div style="background-color: #f6f8fa; padding: 16px; border-left: 4px solid #0366d6; margin-top: 10px; border-radius: 4px;">

* **1단계: 자연어 $\to$ 수식 번역 과정**:
  
  * "개체 수의 시간 변화율" $\implies \frac{dN}{dt}$
  * "현재 개체 수에 비례한 자연 증가" $\implies rN$
  * "환경 저항 인자": 개체 수 비율 $\frac{N}{K}$가 커질수록 성장을 깎아내려야 하므로 $\left(1 - \frac{N}{K}\right)$ 인자를 도입합니다.
  * **로지스틱 미분 방정식**: $\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)$

* **2단계: 식의 거동 정성 분석 (방정식을 풀지 않고 읽기)**:
  
  1. $N \ll K$: $\frac{N}{K} \approx 0 \implies \frac{dN}{dt} \approx rN$ (초기에는 J자형 지수 생장)
  2. $N \to K$: $\left(1 - \frac{N}{K}\right) \to 0 \implies \frac{dN}{dt} \to 0$ (기울기가 $0$으로 평탄화되며 포화)

* **3단계: 미분형 단위 분석**:
  
  * $\left[\frac{dN}{dt}\right] = \frac{[N]}{[t]} = \frac{\text{마리}}{\text{일}}$
  * $[r] = \text{일}^{-1}$ (개체당 하루 번식률)
  * $[K] = \text{마리}$ (환경이 최대로 버틸 수 있는 개체 수)
  * $\left[\frac{N}{K}\right] = \frac{\text{마리}}{\text{마리}} = 1$ (무차원 비율이므로 $1 - N/K$ 전체가 무차원 가중치)

</div>
</details>

---

### 📍 [탐구 3-2] [생명과학Ⅰ/심화] 로트카-볼테라 피식-포식 모델: 두 종의 얽힘

* **교과서 원문**: 
  
  > *"토끼(피식자, $x$)와 여우(포식자, $y$)는 서로의 개체 수에 영향을 미친다. 토끼는 풀을 먹고 자체적으로 번식($\alpha$)하지만, 여우를 만날 확률에 비례($\beta$)하여 잡아먹힌다. 반면 여우는 먹이인 토끼가 없으면 굶어 죽어 자연 감소($\gamma$)하지만, 토끼를 사냥하는 빈도에 비례($\delta$)하여 에너지를 얻고 번식한다."*

**[문항 3-2-1: 문장별 연립 미분 방정식 번역 조립]**

1. **토끼(피식자 $x$)의 변화율 $\frac{dx}{dt}$ 조립**:
   * "토끼의 자체 번식" $\implies$ ( $\qquad$ )
   * "여우와 마주칠 확률($xy$)에 비례하여 잡아먹힘" $\implies -$ ( $\qquad$ )
   * $\implies \frac{dx}{dt} =$ ( $\qquad$ )
2. **여우(포식자 $y$)의 변화율 $\frac{dy}{dt}$ 조립**:
   * "토끼를 사냥하는 빈도($xy$)에 비례하여 번식" $\implies +$ ( $\qquad$ )
   * "먹이가 없어 굶어 죽음" $\implies -$ ( $\qquad$ )
   * $\implies \frac{dy}{dt} =$ ( $\qquad$ )

**[문항 3-2-2: 결합 항 $xy$와 매개변수의 차원 분석]**  
토끼 수 $x$($\text{토끼}$), 여우 수 $y$($\text{여우}$), 시간 $t$($\text{년}$)일 때:

* 결합 항 $xy$의 단위: ( $\qquad$ )
* 포식률 $\beta$와 번식 효율 $\delta$의 단위: $[\beta] =$ ( $\qquad$ ), $[\delta] =$ ( $\qquad$ )

**[문항 3-2-3: 위상 평면과 주기적 진동]**  
제1차 세계대전 당시 지중해 아드리아해에서 어로가 중단되었을 때, 초식 물고기보다 상어(포식자)의 비율이 급증했던 생태학적 미스터리를 로트카-볼테라 모델의 '닫힌 궤도(Closed Orbit)' 특성과 연결하여 설명하시오.

<details class="insight-box">
<summary style="cursor: pointer; font-weight: bold; color: #0366d6; margin-top: 10px;">💡 [탐구 3-2] 문장 수식화 단계별 해설 및 생태 동역학 보기 (클릭)</summary>
<div style="background-color: #f6f8fa; padding: 16px; border-left: 4px solid #0366d6; margin-top: 10px; border-radius: 4px;">

* **1단계: 자연어 $\to$ 연립 미분 방정식 번역 과정**:
  $$ \begin{cases}
  \displaystyle \frac{dx}{dt} = \underbrace{\alpha x}_{\text{토끼 자체 번식}} - \underbrace{\beta xy}_{\text{포식 만남에 의한 피식}} \\[10pt]
  \displaystyle \frac{dy}{dt} = \underbrace{\delta xy}_{\text{사냥을 통한 번식}} - \underbrace{\gamma y}_{\text{기아 자연 사망}}
  \end{cases} $$

* **2단계: 미분형 단위 및 결합 항 분석**:
  
  * 결합 항 $xy$의 단위: $[xy] = \text{토끼} \cdot \text{여우}$ (화학 반응의 분자 충돌과 동일한 질량 작용의 법칙)
  * 토끼 사망 항: $[\beta xy] = [\beta] \times (\text{토끼} \cdot \text{여우}) = \frac{\text{토끼}}{\text{년}} \implies [\beta] = \text{여우}^{-1} \cdot \text{년}^{-1}$
  * 여우 번식 항: $[\delta xy] = [\delta] \times (\text{토끼} \cdot \text{여우}) = \frac{\text{여우}}{\text{년}} \implies [\delta] = \text{토끼}^{-1} \cdot \text{년}^{-1}$

* **3단계: 지성사적 맥락 (아드리아해 어획량 미스터리)**:
  
  * 전쟁으로 인간의 어획이 멈추자, 두 종 모두에게 가해지던 외생적 사망률이 제거되었습니다.
  * 위상 평면상에서 두 종은 고정된 숫자로 수렴하지 않고 타원형의 **'닫힌 궤도(Closed Orbit)'**를 그리며 주기적으로 진동합니다. 볼테라는 어획 중단이 생태계 진동 주기상 포식자(상어)가 극대화되는 위상을 촉발했음을 수학적으로 증명했습니다.

</div>
</details>

---

### 📍 [탐구 3-3] [보건 & 역학] 감염병 SIR 모델: 직관적 상태 정의와 인구 보존

* **상황 서술 (직관적 3대 집단)**: 
  
  > *"외부 유입이 없는 도시의 초기 인구 $N$명은 감염병 유행 기간 동안 다음 세 그룹으로 분류되어 추적된다.*
  > * * **$S(t)$ [감염 가능군 / Susceptible]**: 아직 병에 걸리지 않아 바이러스에 노출되면 감염될 수 있는 건강한 사람*
  > * * **$I(t)$ [전파 감염자 / Infectious]**: 현재 체내에 바이러스가 있어 스스로 앓으며 타인에게 옮길 수 있는 사람*
  > * * **$R(t)$ [완치·제외군 / Recovered]**: 병을 이겨내고 면역을 얻었거나, 격리·치료(또는 사망)되어 **전파 사슬에서 제외된 사람**의 누적 합
  > - 신규 감염은 아직 걸리지 않은 사람($S$)과 전파 감염자($I$)가 마주칠 때 전파율 $\beta$로 발생하여 감염 가능군을 감소시킨다. 감염자는 매일 회복률 $\gamma$의 속도로 제외군($R$)으로 이동한다."

**[문항 3-3-1: 구문별 1:1 수식화]**

1. "감염 가능군 $S$가 $I$와의 접촉($SI$)으로 감염되어 감소함" $\implies \frac{dS}{dt} =$ ( $\qquad$ )
2. "새로 감염된 사람($\beta SI$)에서 회복되어 빠져나간 사람($\gamma I$)을 뺀 감염자 수의 알짜 변화율" $\implies \frac{dI}{dt} =$ ( $\qquad$ )
3. "감염자 중 회복·제외되어 새로 누적된 사람" $\implies \frac{dR}{dt} =$ ( $\qquad$ )

**[문항 3-3-2: 인구 보존 법칙 유도]**  
세 미분 방정식을 변변 더하여 $\frac{dS}{dt} + \frac{dI}{dt} + \frac{dR}{dt}$의 값을 구하고, 양변을 적분하여 전체 인구가 보존됨($S+I+R=N$)을 증명하시오.

**[문항 3-3-3: 대유행 조건과 기본재생산지수($R_0$)]**  
감염자 수가 증가($\frac{dI}{dt} > 0$)하기 위한 감염 가능군 $S$의 조건을 구하고, $R_0 = \frac{\beta N}{\gamma}$의 단위 연산을 통해 $R_0$가 무차원 수임을 보이시오.

<details class="insight-box">
<summary style="cursor: pointer; font-weight: bold; color: #0366d6; margin-top: 10px;">💡 [탐구 3-3] 문장 수식화 단계별 해설 및 역학 동역학 보기 (클릭)</summary>
<div style="background-color: #f6f8fa; padding: 16px; border-left: 4px solid #0366d6; margin-top: 10px; border-radius: 4px;">

* **1단계: 자연어 $\to$ SIR 3원 연립 미분 방정식 번역 과정**:
  $$ \begin{cases}
  \displaystyle \frac{dS}{dt} = -\beta SI \\[8pt]
  \displaystyle \frac{dI}{dt} = \beta SI - \gamma I = (\beta S - \gamma)I \\[8pt]
  \displaystyle \frac{dR}{dt} = \gamma I
  \end{cases} $$

* **2단계: 인구 보존 법칙(Conservation Law)의 적분형 유도**:
  $$ \frac{dS}{dt} + \frac{dI}{dt} + \frac{dR}{dt} = -\beta SI + (\beta SI - \gamma I) + \gamma I = 0 $$
  시간 변화율의 합이 $0$이므로 양변을 적분하면:
  $$ \int \left(\frac{dS}{dt} + \frac{dI}{dt} + \frac{dR}{dt}\right) dt = \int 0 \, dt \implies S(t) + I(t) + R(t) = N_0 \quad (\text{초기 코호트 불변}) $$

* **3단계: 대유행 조건 및 $R_0$ 무차원성**:
  
  * 감염 확산: $\frac{dI}{dt} = (\beta S - \gamma)I > 0 \iff S > \frac{\gamma}{\beta}$
  * 초기 $S \approx N$ 대입: $R_0 = \frac{\beta N}{\gamma} > 1$ 일 때 대유행 발생.
  * **단위 검증**: $[\beta] = \text{명}^{-1} \cdot \text{일}^{-1}$, $[\gamma] = \text{일}^{-1}$, $[N] = \text{명}$
    $$ [R_0] = \frac{(\text{명}^{-1} \cdot \text{일}^{-1}) \times \text{명}}{\text{일}^{-1}} = \frac{\text{일}^{-1}}{\text{일}^{-1}} = 1 \quad (\mathbf{무차원\ 증폭\ 배수!}) $$

</div>
</details>

---

### 📍 [탐구 3-4] [심화 확장] 페스트의 역설과 SIR에서 SIRD 모델로의 진화

* **역사적 의문**: 
  
  > *"1905년 봄베이의 페스트(흑사병) 유행 당시 치명률은 90%에 달했다. 수많은 시민이 사망했는데, 어떻게 세 집단의 합이 일정하다($S + I + R = N$)며 '전체 인구수가 보존된다'고 서술할 수 있는가?"*

**[문항 3-4-1: 역사적 원전 분석]**  
1927년 커맥-맥켄드릭 논문에서 $R$이 왜 'Recovered(완치자)'가 아닌 **'Removed(제외군)'**로 명명되었는지 서술하시오.

**[문항 3-4-2: SIRD 4원 연립 미분 방정식 조립]**  
전파 감염자($I$)의 이탈 경로를 **순수 완치·항체 획득자($R$)**와 **누적 사망자($D$, Deceased)**로 분리하여 SIRD 4원 연립 미분 방정식을 완성하시오. (완치율 $\gamma$, 치명 사망률 $\mu$)

**[문항 3-4-3: 두 가지 인구 개념의 수식적 구별]**  

* '닫힌 코호트의 상태 보존' 수식: $\frac{dS}{dt} + \frac{dI}{dt} + \frac{dR}{dt} + \frac{dD}{dt} =$ ( $\qquad$ )
* '실제 도시의 생존 인구 $N_{\text{alive}}(t) = S + I + R$'의 시간 변화율: $\frac{dN_{\text{alive}}}{dt} =$ ( $\qquad$ )

<details class="insight-box">
<summary style="cursor: pointer; font-weight: bold; color: #0366d6; margin-top: 10px;">💡 [탐구 3-4] 페스트 역설 해소 및 SIRD 모델 해설 보기 (클릭)</summary>
<div style="background-color: #f6f8fa; padding: 16px; border-left: 4px solid #0366d6; margin-top: 10px; border-radius: 4px;">

* **1단계: 역사적 진실과 어원**:
  
  * 커맥과 맥켄드릭이 사용한 데이터는 완치자 수가 아니라 매주 보고된 **'페스트 사망자 통계'**였습니다.
  * 따라서 원전에서 $R$은 "사망, 완치, 격리에 의해 전파 사슬에서 제거·제외된 자(Removed from the infectious process)"를 의미했습니다.
  * 즉, $S+I+R=N$은 살아있는 사람이 줄지 않는다는 뜻이 아니라 **"초기 인원 $N$명 전원의 상태(행방)를 수학적으로 누락 없이 추적한다"는 닫힌 상태 공간의 보존**을 뜻합니다.

* **2단계: SIRD 4원 연립 미분 방정식 (현실적 모델로의 진화)**:
  $$ \begin{cases}
  \displaystyle \frac{dS}{dt} = -\beta SI \\[8pt]
  \displaystyle \frac{dI}{dt} = \beta SI - (\gamma + \mu)I = [\beta S - (\gamma + \mu)]I \\[8pt]
  \displaystyle \frac{dR}{dt} = \gamma I \quad (\text{순수 완치, 면역 획득자}) \\[8pt]
  \displaystyle \frac{dD}{dt} = \mu I \quad (\text{누적 사망자})
  \end{cases} $$

* **3단계: 두 가지 인구 개념의 수학적 구별**:
  
  1. **초기 코호트 총량 보존**: $\frac{dS}{dt} + \frac{dI}{dt} + \frac{dR}{dt} + \frac{dD}{dt} = 0 \implies S(t) + I(t) + R(t) + D(t) = N_0$
  2. **실제 살아있는 인구 ($N_{\text{alive}} = S + I + R$)**:
     $$ \frac{dN_{\text{alive}}}{dt} = \frac{dS}{dt} + \frac{dI}{dt} + \frac{dR}{dt} = -\mu I < 0 $$
     감염자($I > 0$)와 치명률($\mu > 0$)이 존재하는 한, **실제 생존 인구는 매 순간 사망률($\mu I$)만큼 가파르게 감소**합니다.

</div>
</details>

---

## Step 4. [지구과학] 시간적 붕괴와 공간적 구배(Gradient)

### 📍 [탐구 4-1] 방사성 동위원소 붕괴: '현재 잔여량에 비례'

* **교과서 원문**: 
  
  > *"방사성 동위원소의 붕괴 속도는 온도나 압력 등 외부 환경에 영향을 받지 않으며, 오직 현재 남아 있는 방사성 동위원소의 개수($N$)에 비례하여 감소한다."*

**[문항 4-1-1: 교과서 문장 수식화]**

1. "시간 $t$에 따른 방사성 동위원소 개수 $N$의 붕괴 속도(감소율)" $\implies -\frac{dN}{dt}$
2. "현재 남아 있는 개수 $N$에 비례 (붕괴상수 $\lambda$)" $\implies \lambda N$
3. 미분 방정식 완성: $\frac{dN}{dt} =$ ( $\qquad$ )

**[문항 4-1-2: 학문 간 대칭성 통찰]**  
이 방정식은 앞서 배운 [화학 1차 반응속도식 $-\frac{d[A]}{dt} = k[A]$]과 어떤 대수적 대칭성을 가지며, 왜 두 현상 모두 지수 감쇠($e^{-\lambda t}$)를 따르는지 설명하시오.

<details class="insight-box">
<summary style="cursor: pointer; font-weight: bold; color: #0366d6; margin-top: 10px;">💡 [탐구 4-1] 문장 수식화 단계별 해설 보기 (클릭)</summary>
<div style="background-color: #f6f8fa; padding: 16px; border-left: 4px solid #0366d6; margin-top: 10px; border-radius: 4px;">

* **수식화 모델**: $\frac{dN}{dt} = -\lambda N$
* **해석학적 통찰**: 화학 반응의 분자 결합 파괴이든, 지구과학의 원자핵 자연 붕괴이든, **"변화율이 자기 자신의 현재 크기에 정비례하는 선형 1계 미분 시스템"**은 자연계 어디서나 완벽히 동일한 지수 감쇠 법칙($N(t) = N_0 e^{-\lambda t}$)을 공유합니다.

</div>
</details>

---

### 📍 [탐구 4-2] 해양의 수온 약층: 시간에 대한 미분에서 '공간'에 대한 미분으로!

* **교과서 원문**: 
  
  > *"수온 약층은 수심이 깊어질수록 수온이 급격히 낮아지는 층이다. 저위도 해역에서는 표층 수온이 높아 깊이에 따른 온도 변화가 매우 크며, 이 층은 혼합층과 심해층 사이의 물질 교환을 차단하는 안정된 층 역할을 한다."*

**[문항 4-2-1: 공간 도함수로의 번역]**

1. "수심($z$)에 따른 수온($T$)의 순간 변화율 (공간 구배)" $\implies$ ( $\qquad$ )
2. 해양 3개 층의 공간 도함수 정성 모델링:
   * **혼합층 (바람으로 균일)**: $\frac{dT}{dz} \approx$ ( $\qquad$ )
   * **수온 약층 (급격한 온도 저하)**: $\frac{dT}{dz} \mathrel{<} 0$ (절댓값 극대)
   * **심해층 (차갑고 균일)**: $\frac{dT}{dz} \approx$ ( $\qquad$ )

**[문항 4-2-2: 공간 구배의 적분형 단위 검증]**  
수온 단위 $^{\circ}\mathrm{C}$, 수심 단위 $\mathrm{m}$일 때, 두 수심 $z_1, z_2$ 사이의 총 수온 차이 식 $T(z_2) - T(z_1) = \int_{z_1}^{z_2} \frac{dT}{dz} \, dz$의 적분형 단위를 연산하여 온도 단위가 복원됨을 보이시오.

<details class="insight-box">
<summary style="cursor: pointer; font-weight: bold; color: #0366d6; margin-top: 10px;">💡 [탐구 4-2] 공간 구배 수식화 및 차원 분석 보기 (클릭)</summary>
<div style="background-color: #f6f8fa; padding: 16px; border-left: 4px solid #0366d6; margin-top: 10px; border-radius: 4px;">

* **1단계: 공간 도함수 번역**:
  
  * "깊이 $z$에 따른 수온 $T$의 순간 변화율" $\implies \frac{dT}{dz}$
  * 미분형 단위: $\left[\frac{dT}{dz}\right] = \frac{[T]}{[z]} = \frac{^{\circ}\mathrm{C}}{\mathrm{m}}$ ($\text{깊이 } 1\,\mathrm{m}\text{당 수온 강하율}$)

* **2단계: 해양 3개 층의 도함수 값**:
  
  * 혼합층: $\frac{dT}{dz} \approx 0$ (바람에 의한 역학적 혼합으로 수온 일정)
  * 수온 약층: $\frac{dT}{dz} \ll 0$ (기울기 절댓값이 큼 $\implies$ 상층은 가볍고 하층은 무거워 연직 대류가 극도로 억제되는 강력한 유체역학적 안정층)
  * 심해층: $\frac{dT}{dz} \approx 0$ (태양 복사가 도달하지 않는 균일 저온층)

* **3단계: 적분형 단위 연산 (순변화량 복원)**:
  $$ \left[\int_{z_1}^{z_2} \frac{dT}{dz} \, dz\right] = \left[\frac{dT}{dz}\right] \times [z] = \frac{^{\circ}\mathrm{C}}{\mathrm{m}} \times \mathrm{m} = ^{\circ}\mathrm{C} = [T(z_2) - T(z_1)] $$

</div>
</details>


## 📝 [학생 탐구 활동지] 교과서 문장을 미분 방정식으로 번역하기

| 학년 / 반     | 학번  | 이름  | 모둠명 | 지도교사 확인 |
|:----------:|:---:|:---:|:---:|:-------:|
| 2/3학년 ( )반 |     |     |     |         |

---

### [원리] 교과서 문장 $\to$ 수식 번역 및 단위 대칭성 규칙

1. "시간 $t$에 따른 $A$의 변화율" $\implies \underline{\hspace{3cm}}$, 미분형 단위 규칙: $\left[\frac{dA}{dt}\right] = \underline{\hspace{3cm}}$
2. "구간 $[t_1, t_2]$ 동안 누적된 총 변화량" $\implies \int_{t_1}^{t_2} \underline{\hspace{2.5cm}} \, dt$, 적분형 단위 규칙: $\left[\int y\,dx\right] = \underline{\hspace{3cm}}$

---

### 1. 물리학: 교과서 문장 분해와 운동·장 모델링

#### [활동 1-1] 뉴턴 제2법칙의 문장 분해

> *"속도는 시간에 따른 위치의 변화율이며, 가속도는 시간에 따른 속도의 변화율이다. 물체의 가속도는 작용하는 알짜힘에 비례하고 질량에 반비례한다."*

* **문장 1**: "시간에 따른 위치($x$)의 변화율" $\implies v(t) = \underline{\hspace{4cm}}$
* **문장 2**: "시간에 따른 속도($v$)의 변화율" $\implies a(t) = \underline{\hspace{4cm}}$
* **문장 3**: "가속도는 알짜힘($F$)에 비례하고 질량($m$)에 반비례" $\implies a = \underline{\hspace{4cm}}$
* **방정식 결합 (2계 상미분 방정식)**: $F = \underline{\hspace{5cm}}$
* **단위 검증**: 가속도의 미분형 단위 $\left[\frac{dv}{dt}\right] = \underline{\hspace{3cm}}$, 정적분 $\int a\,dt$의 적분형 단위: $\underline{\hspace{3cm}}$

#### [활동 1-2] 패러데이 법칙과 렌츠의 부호

> *"폐회로에 유도되는 기전력($\mathcal{E}$)은 폐회로를 통과하는 자기선속($\Phi_B$)의 시간에 따른 변화율에 비례하며, 그 변화를 방해하는 방향으로 유도된다. 코일 감은 수($N$)에 비례한다."*

* "자기선속의 시간에 따른 변화율": $\underline{\hspace{3.5cm}}$ / "방해하는 방향": $\underline{\hspace{1.5cm}}$ / "감은 수 비례": $\underline{\hspace{1.5cm}}$
* **미분 방정식 완성**: $\mathcal{E} = \underline{\hspace{6cm}}$
* $[\Phi_B] = \mathrm{Wb} = \mathrm{V \cdot s}$일 때 미분형 단위 연산으로 $[\mathcal{E}] = \mathrm{V}$임을 증명하시오:
  
  > $\underline{\hspace{12cm}}$

#### [활동 1-3] 뉴턴의 냉각 법칙

> *"물체의 온도 변화율은 물체의 온도($T$)와 환경 온도($T_{\text{env}}$)의 차이에 비례한다."*

* "시간에 따른 온도 변화율": $\underline{\hspace{3cm}}$ / "온도 차이": $\underline{\hspace{3cm}}$ / "식어감(감소)": $\underline{\hspace{1.5cm}}$
* **미분 방정식 완성**: $\frac{dT}{dt} = \underline{\hspace{5cm}}$
* 냉각 계수 $k$의 단위: $[k] = \underline{\hspace{3cm}}$ / 지수항 $e^{-kt}$에서 거듭제곱수가 무차원인 이유: $\underline{\hspace{5cm}}$

---

### 2. 화학: 반응 속도의 부호와 반감기의 차원 검증

> *"반응 속도($v$)는 시간에 따른 반응물 농도($[A]$)의 감소율로 정의된다. 1차 반응에서 반응 속도는 반응물의 농도에 정비례한다."*

1. **정의의 수식화**: $v = -\frac{d[A]}{dt} = \underline{\hspace{4cm}}$ (단, 속도상수 $k$)
2. 농도 단위 $\mathrm{M} = \mathrm{mol/L}$, 시간 단위 $\mathrm{s}$일 때:
   * 반응 속도 $v$의 미분형 단위: $[v] = \underline{\hspace{4cm}}$
   * 1차 반응 속도상수 단위: $[k] = \underline{\hspace{4cm}}$, 2차 반응($v = k[A]^2$) 속도상수 단위: $[k] = \underline{\hspace{4cm}}$
3. 1차 반응 반감기 공식 $t_{1/2} = \frac{\ln 2}{k}$에서 초기 농도가 소거되는 수학적 이유를 적으시오:
   
   > $\underline{\hspace{14cm}}$

---

### 3. 생명과학 & 역학: 다원 연립 미분 방정식으로의 도약

#### [활동 3-1] 개체군 생장과 로지스틱 환경 저항

> *"자원이 충분할 때는 개체 수($N$)의 번식에 비례하여 기하급수적으로 증가하지만, 환경 수용 능력($K$)에 도달할수록 환경 저항으로 인해 증가율이 $0$에 수렴한다."*

* **무제한 J자형 생장식**: $\frac{dN}{dt} = \underline{\hspace{4cm}}$
* **환경 저항 인자**: $\underline{\hspace{3cm}}$ $\implies$ **로지스틱 미분 방정식**: $\frac{dN}{dt} = \underline{\hspace{6cm}}$

#### [활동 3-2] 로트카-볼테라 피식-포식 모델의 문장 조립

> *"토끼($x$)는 자체 번식($\alpha$)하지만 여우를 만날 확률($xy$)에 비례하여 잡아먹힌다($\beta$). 여우($y$)는 토끼 사냥 빈도($xy$)에 비례하여 번식($\delta$)하지만, 먹이가 없으면 굶어 죽는다($\gamma$)."*

* 피식자(토끼)의 변화율: $\frac{dx}{dt} = \underline{\hspace{3.5cm}} - \underline{\hspace{3.5cm}}$
* 포식자(여우)의 변화율: $\frac{dy}{dt} = \underline{\hspace{3.5cm}} - \underline{\hspace{3.5cm}}$
* 포식률 $\beta$의 단위: $[\beta] = \underline{\hspace{4cm}}$, 여우 번식 효율 $\delta$의 단위: $[\delta] = \underline{\hspace{4cm}}$

#### [활동 3-3] 감염병 SIR 모델과 직관적 상태 정의

* **$S(t)$ [감염 가능군]**: 아직 안 걸려 걸릴 수 있는 사람 / **$I(t)$ [전파 감염자]**: 현재 앓으며 남에게 옮기는 사람 / **$R(t)$ [완치·제외군]**: 전파 사슬에서 제외된 사람
* **SIR 3원 연립 미분 방정식 완성**:
  $$\frac{dS}{dt} = \underline{\hspace{3.5cm}}, \quad \frac{dI}{dt} = \underline{\hspace{3.5cm}}, \quad \frac{dR}{dt} = \underline{\hspace{3.5cm}}$$
* **인구 보존 법칙 유도**: $\frac{dS}{dt} + \frac{dI}{dt} + \frac{dR}{dt} = \underline{\hspace{3cm}} \implies S(t)+I(t)+R(t) = \underline{\hspace{2cm}}$
* 기본재생산지수 $R_0 = \frac{\beta N}{\gamma}$의 단위 연산을 통해 이것이 무차원 수임을 보이시오:
  
  > $\underline{\hspace{12cm}}$

#### [활동 3-4] [심화 탐구] 페스트의 역설과 SIRD 4원 모델

* "흑사병으로 수많은 사람이 사망하는데, 왜 세 집단의 합($S+I+R=N$)이 일정하다고 할까?" 역사적 진실을 바탕으로 답하시오:
  
  > $\underline{\hspace{14cm}}$
* 완치자($R$)와 누적 사망자($D$, 치명률 $\mu$)를 분리한 **SIRD 연립 방정식**:
  $$\frac{dS}{dt} = \underline{\hspace{3cm}}, \quad \frac{dI}{dt} = \underline{\hspace{3cm}}$$
  $$\frac{dR}{dt} = \underline{\hspace{3cm}}, \quad \frac{dD}{dt} = \underline{\hspace{3cm}}$$
* 실제 도시 생존 인구 $N_{\text{alive}}(t) = S + I + R$의 시간 변화율: $\frac{dN_{\text{alive}}}{dt} = \underline{\hspace{4cm}}$

---

### 4. 지구과학: 공간 구배(Gradient)의 적분

> *"수온 약층은 수심($z$)이 깊어질수록 수온($T$)이 급격히 낮아지는 층이다."*

1. 공간 구배 기호: $\underline{\hspace{3cm}}$, 미분형 단위: $\left[\frac{dT}{dz}\right] = \underline{\hspace{3cm}}$
2. 두 수심 $z_1, z_2$ 사이의 총 수온 차이 적분식: $T(z_2) - T(z_1) = \int_{z_1}^{z_2} \underline{\hspace{3cm}} \, dz$


## 📚 [교사용 심화 가이드] 교과서 문장 수식화 지도법 및 통섭적 지성사

### 1. 교과서 문장 $\to$ 미분 방정식 번역 지도 전략 (Scaffolding)

학생들이 자연어 문장을 미분 방정식으로 번역할 때 가장 빈번하게 범하는 오개념과 이를 지도하는 발문 전략입니다.

| 학생의 흔한 번역 오류                             | 원인 분석               | 교사의 스캐폴딩 발문 가이드                                                                                         |
|:---------------------------------------- |:------------------- |:------------------------------------------------------------------------------------------------------- |
| **"비례한다"를 덧셈($+$)으로 착각**                 | 증가한다는 일상 표현과 혼동     | "비례한다는 것은 $B$가 2배, 3배가 될 때 변화율도 2배, 3배가 된다는 뜻이야. 그러려면 덧셈이 아니라 어떤 연산(곱셈)과 비례상수($k$)가 필요할까?"              |
| **감소·방해 서술에서 음수($-$) 부호 누락**             | 도함수 자체의 크기에만 집중     | "온도가 식거나 반응물이 사라진다면, 나중 값에서 처음 값을 뺀 변화량($\Delta y$)의 부호는 무엇일까? 도함수가 음수여야 하니 앞에 $-$를 붙여야겠지?"             |
| **상태 변수($y$)와 변화율($\frac{dy}{dt}$)의 혼동** | 현재 상태와 변화 속도를 구별 못함 | "지금 물체의 온도가 높은 것($T$)과 온도가 빠르게 떨어지는 것($\frac{dT}{dt}$)은 어떻게 다를까? 문장에서 '변화율'이라는 단어를 찾아 도함수 기호로 먼저 바꿔보자." |
| **다집단 상호작용에서 덧셈($x+y$) 적용**              | 만남의 확률을 직관적으로 합산함   | "복도에서 1학년($x$명)과 2학년($y$명)이 마주칠 확률은 두 학년 인원수의 합일까, 아니면 경우의 수(곱셈)일까? 화학의 분자 충돌과 같단다."                    |

---

### 2. 주요 모델별 미분형·적분형 단위 총괄 요약표

| 모델명         | 미분 방정식                                     | 핵심 매개변수              | 매개변수의 물리 단위                                                        | 차원 일치 및 무차원 수 판별식                                                                             |
|:----------- |:------------------------------------------ |:--------------------:|:------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------- |
| **뉴턴 운동**   | $F = m\frac{dv}{dt}$                       | $m$                  | $\mathrm{kg}$                                                      | $[F] = [m]\frac{[v]}{[t]} = \mathrm{kg \cdot m/s^2} = \mathrm{N}$                             |
| **패러데이 유도** | $\mathcal{E} = -N\frac{d\Phi_B}{dt}$       | $N$                  | 무차원 ($1$)                                                          | $[\mathcal{E}] = \frac{[\Phi_B]}{[t]} = \frac{\mathrm{V \cdot s}}{\mathrm{s}} = \mathrm{V}$   |
| **뉴턴 냉각**   | $\frac{dT}{dt} = -k(T - T_{\text{env}})$   | $k$                  | $\mathrm{s^{-1}}$                                                  | 지수항 $[kt] = \mathrm{s^{-1}} \times \mathrm{s} = 1$ (무차원)                                      |
| **화학 1차**   | $v = -\frac{d[A]}{dt} = k[A]$              | $k$                  | $\mathrm{s^{-1}}$                                                  | 반감기 $[t_{1/2}] = [1/k] = \mathrm{s}$                                                          |
| **화학 2차**   | $v = k[A]^2$                               | $k$                  | $\mathrm{M^{-1} \cdot s^{-1}}$                                     | $[k] = \frac{[v]}{[[A]]^2} = \frac{\mathrm{M/s}}{\mathrm{M^2}} = \mathrm{M^{-1}\cdot s^{-1}}$ |
| **로지스틱**    | $\frac{dN}{dt} = rN(1 - N/K)$              | $r, K$               | $[r]=\text{일}^{-1}, [K]=\text{마리}$                                 | $[N/K] = 1$ (무차원 수용 인자)                                                                       |
| **피식-포식**   | $\frac{dx}{dt} = \alpha x - \beta xy$      | $\alpha, \beta$      | $[\alpha]=\text{년}^{-1}, [\beta]=\text{여우}^{-1}\cdot\text{년}^{-1}$ | 결합 항 $[xy]$를 통해 좌변 단위($\text{토끼/년}$)로 변환                                                      |
| **SIR 모델**  | $\frac{dI}{dt} = \beta SI - \gamma I$      | $\beta, \gamma$      | $[\beta]=\text{명}^{-1}\cdot\text{일}^{-1}, [\gamma]=\text{일}^{-1}$  | 기본재생산지수 $[R_0] = [\frac{\beta N}{\gamma}] = 1$ (무차원 지수)                                       |
| **SIRD 모델** | $\frac{dI}{dt} = \beta SI - (\gamma+\mu)I$ | $\beta, \gamma, \mu$ | $[\mu] = \text{일}^{-1}$ (치명 사망률)                                   | $[R_0] = [\frac{\beta N}{\gamma+\mu}] = 1$ (무차원 지수)                                           |

---

### 3. 지성사적 배경 스토리 및 심화 지도 팁

#### ① 아드리아해 어획량 미스터리와 볼테라 (피식-포식 모델)

제1차 세계대전으로 어업이 중단되었을 때 초식 어류보다 포식자(상어)가 급증한 현상은, 인간의 어획 행위가 두 종 모두에게 가하던 인위적 사망률이 일시에 걷히면서 생태계 위상 평면(Phase Plane)의 닫힌 궤도 상에서 포식자가 번성하는 위상으로 회전했기 때문입니다. 볼테라는 결합 항 $\beta xy$를 통해 이 역설을 증명했습니다.

#### ② 봄베이 흑사병의 진실과 SIR에서 SIRD로의 진화

* **오해의 근원**: $S+I+R=N$에서 인구수 보존을 '살아있는 인구의 불변'으로 오해하면 치명적 전염병(페스트)과 정면 충돌합니다. 커맥과 맥켄드릭의 1927년 논문 원전에서 $R$은 'Recovered'가 아니라 **'Removed(사망, 완치, 격리로 전파 사슬에서 제외된 자)'**였습니다.
* **SIRD 모델 지도 전략**: 학생들에게 완치자($R$)와 사망자($D$)를 분리해 보도록 유도하면, 전체 닫힌 코호트의 총량 보존($\frac{dS}{dt}+\frac{dI}{dt}+\frac{dR}{dt}+\frac{dD}{dt}=0$)과 실제 살아있는 인구의 감소($\frac{dN_{\text{alive}}}{dt} = -\mu I < 0$)를 명쾌하게 구별하게 됩니다. 이를 통해 학생들은 수학적 모델이 현실의 비극과 과학적 데이터를 얼마나 정직하게 담아내는지 체감할 수 있습니다.

