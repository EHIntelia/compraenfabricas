/* @ds-bundle: {"format":4,"namespace":"CompraEnFBricasDesignSystem_e5b2dc","components":[{"name":"Accordion","sourcePath":"components/content/Accordion.jsx"},{"name":"Card","sourcePath":"components/content/Card.jsx"},{"name":"CheckItem","sourcePath":"components/content/CheckItem.jsx"},{"name":"PeachBox","sourcePath":"components/content/PeachBox.jsx"},{"name":"PricingCard","sourcePath":"components/content/PricingCard.jsx"},{"name":"Badge","sourcePath":"components/core/Badge.jsx"},{"name":"Button","sourcePath":"components/core/Button.jsx"},{"name":"GradientText","sourcePath":"components/core/GradientText.jsx"},{"name":"Logo","sourcePath":"components/core/Logo.jsx"},{"name":"Checkbox","sourcePath":"components/forms/Checkbox.jsx"},{"name":"Input","sourcePath":"components/forms/Input.jsx"},{"name":"Radio","sourcePath":"components/forms/Radio.jsx"},{"name":"Select","sourcePath":"components/forms/Select.jsx"}],"sourceHashes":{"components/content/Accordion.jsx":"91b601e2ed0f","components/content/Card.jsx":"d3f2cb0cfaa7","components/content/CheckItem.jsx":"aa83253c8cfc","components/content/PeachBox.jsx":"02517a2da987","components/content/PricingCard.jsx":"3a0e152ff66b","components/core/Badge.jsx":"0e70b7eadc09","components/core/Button.jsx":"0f56b9c70609","components/core/GradientText.jsx":"b352c1a6a269","components/core/Logo.jsx":"29beba828b98","components/forms/Checkbox.jsx":"5aa83c8480cd","components/forms/Input.jsx":"f1db94eebb23","components/forms/Radio.jsx":"e6a3d1d60ebd","components/forms/Select.jsx":"e2bf35bd3bee","ui_kits/landing/Landing.jsx":"6cf8a5ed5db0","ui_kits/landing/Register.jsx":"413a70fe1722"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.CompraEnFBricasDesignSystem_e5b2dc = window.CompraEnFBricasDesignSystem_e5b2dc || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/content/Accordion.jsx
try { (() => {
function Accordion({
  items = [],
  defaultOpen = -1
}) {
  const [o, setO] = React.useState(defaultOpen);
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gap: 10,
      fontFamily: 'var(--font-sans)'
    }
  }, items.map((it, i) => {
    const open = o === i;
    return /*#__PURE__*/React.createElement("div", {
      key: i,
      style: {
        background: '#fff',
        border: '1px solid ' + (open ? 'var(--cef-naranja)' : 'var(--cef-borde)'),
        borderRadius: 'var(--radius-md)',
        overflow: 'hidden',
        transition: 'border-color var(--dur-base)'
      }
    }, /*#__PURE__*/React.createElement("button", {
      onClick: () => setO(open ? -1 : i),
      style: {
        all: 'unset',
        boxSizing: 'border-box',
        width: '100%',
        cursor: 'pointer',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        gap: 12,
        padding: '16px 18px',
        fontWeight: 700,
        fontSize: 16,
        color: 'var(--cef-tinta)'
      }
    }, it.q, /*#__PURE__*/React.createElement("span", {
      style: {
        flex: 'none',
        width: 28,
        height: 28,
        borderRadius: 999,
        background: open ? 'var(--gradient-estrella)' : 'var(--cef-durazno)',
        color: open ? '#fff' : 'var(--cef-naranja-700)',
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontSize: 18,
        transition: 'transform var(--dur-base)',
        transform: open ? 'rotate(45deg)' : 'none'
      }
    }, "+")), open && /*#__PURE__*/React.createElement("div", {
      style: {
        padding: '0 18px 18px',
        color: 'var(--cef-gris)',
        fontSize: 15,
        lineHeight: 1.55
      }
    }, it.a));
  }));
}
Object.assign(__ds_scope, { Accordion });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/content/Accordion.jsx", error: String((e && e.message) || e) }); }

// components/content/Card.jsx
try { (() => {
function Card({
  tone = 'white',
  padding = 24,
  children,
  style
}) {
  const t = {
    white: {
      background: '#fff',
      border: '1px solid var(--cef-borde)'
    },
    cream: {
      background: 'var(--cef-crema)',
      border: '1px solid var(--cef-borde)'
    },
    peach: {
      background: 'var(--cef-durazno)',
      border: '1px solid transparent'
    },
    dark: {
      background: 'var(--cef-tinta)',
      color: '#fff',
      border: '1px solid transparent'
    }
  }[tone];
  return /*#__PURE__*/React.createElement("div", {
    style: {
      borderRadius: 'var(--radius-lg)',
      padding,
      boxShadow: tone === 'white' ? 'var(--shadow-sm)' : 'none',
      fontFamily: 'var(--font-sans)',
      ...t,
      ...style
    }
  }, children);
}
Object.assign(__ds_scope, { Card });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/content/Card.jsx", error: String((e && e.message) || e) }); }

// components/content/CheckItem.jsx
try { (() => {
function CheckItem({
  children,
  style
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 12,
      alignItems: 'flex-start',
      fontFamily: 'var(--font-sans)',
      fontSize: 16,
      lineHeight: 1.45,
      ...style
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      flex: 'none',
      width: 22,
      height: 22,
      borderRadius: 999,
      background: 'var(--gradient-estrella)',
      color: '#fff',
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontSize: 13,
      fontWeight: 700,
      marginTop: 1
    }
  }, "\u2713"), /*#__PURE__*/React.createElement("span", null, children));
}
Object.assign(__ds_scope, { CheckItem });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/content/CheckItem.jsx", error: String((e && e.message) || e) }); }

// components/content/PeachBox.jsx
try { (() => {
function PeachBox({
  title,
  children,
  style
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      background: 'var(--cef-durazno)',
      borderLeft: '5px solid var(--cef-naranja)',
      borderRadius: 'var(--radius-md)',
      padding: '18px 20px',
      fontFamily: 'var(--font-sans)',
      fontSize: 16,
      lineHeight: 1.5,
      color: 'var(--cef-tinta)',
      ...style
    }
  }, title && /*#__PURE__*/React.createElement("div", {
    style: {
      fontWeight: 700,
      color: 'var(--cef-naranja-700)',
      marginBottom: 4
    }
  }, title), children);
}
Object.assign(__ds_scope, { PeachBox });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/content/PeachBox.jsx", error: String((e && e.message) || e) }); }

// components/core/Badge.jsx
try { (() => {
function Badge({
  variant = 'peach',
  children,
  style
}) {
  const v = {
    peach: {
      background: 'var(--cef-durazno)',
      color: 'var(--cef-naranja-700)'
    },
    gradient: {
      background: 'var(--gradient-estrella)',
      color: '#fff'
    },
    dark: {
      background: 'var(--cef-tinta)',
      color: '#fff'
    },
    outline: {
      background: '#fff',
      color: 'var(--cef-naranja-700)',
      boxShadow: 'inset 0 0 0 1.5px var(--cef-naranja-700)'
    },
    success: {
      background: 'var(--cef-verde-bg)',
      color: 'var(--cef-verde)'
    }
  }[variant];
  return /*#__PURE__*/React.createElement("span", {
    style: {
      display: 'inline-flex',
      alignItems: 'center',
      gap: 6,
      fontFamily: 'var(--font-sans)',
      fontWeight: 700,
      fontSize: 12,
      letterSpacing: 'var(--ls-badge)',
      textTransform: 'uppercase',
      padding: '6px 12px',
      borderRadius: 'var(--radius-pill)',
      lineHeight: 1.2,
      whiteSpace: 'nowrap',
      ...v,
      ...style
    }
  }, children);
}
Object.assign(__ds_scope, { Badge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Badge.jsx", error: String((e && e.message) || e) }); }

// components/core/Button.jsx
try { (() => {
const sizes = {
  sm: {
    padding: '10px 18px',
    fontSize: 14
  },
  md: {
    padding: '14px 24px',
    fontSize: 16
  },
  lg: {
    padding: '18px 32px',
    fontSize: 18
  }
};
function Button({
  variant = 'primary',
  size = 'md',
  fullWidth = false,
  disabled = false,
  icon,
  children,
  onClick,
  type = 'button',
  style
}) {
  const [h, setH] = React.useState(false);
  const [p, setP] = React.useState(false);
  const base = {
    display: 'inline-flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    fontFamily: 'var(--font-sans)',
    fontWeight: 700,
    borderRadius: 'var(--radius-pill)',
    border: '2px solid transparent',
    cursor: disabled ? 'not-allowed' : 'pointer',
    width: fullWidth ? '100%' : undefined,
    transition: 'transform var(--dur-fast) var(--ease-out),box-shadow var(--dur-base),background var(--dur-base)',
    transform: p && !disabled ? 'scale(.98)' : 'none',
    opacity: disabled ? .45 : 1,
    lineHeight: 1.2,
    ...sizes[size]
  };
  const v = {
    primary: {
      background: h && !disabled ? 'var(--gradient-estrella-hover)' : 'var(--gradient-estrella)',
      color: '#fff',
      boxShadow: h && !disabled ? '0 10px 28px rgba(234,88,12,.35)' : 'var(--shadow-accent)'
    },
    secondary: {
      background: h && !disabled ? 'var(--cef-durazno)' : '#fff',
      color: 'var(--cef-naranja-700)',
      borderColor: 'var(--cef-naranja)'
    },
    dark: {
      background: h && !disabled ? '#000' : 'var(--cef-tinta)',
      color: '#fff'
    },
    ghost: {
      background: h && !disabled ? 'var(--cef-durazno)' : 'transparent',
      color: 'var(--cef-naranja-700)'
    }
  }[variant];
  return /*#__PURE__*/React.createElement("button", {
    type: type,
    disabled: disabled,
    onClick: onClick,
    onMouseEnter: () => setH(true),
    onMouseLeave: () => {
      setH(false);
      setP(false);
    },
    onMouseDown: () => setP(true),
    onMouseUp: () => setP(false),
    style: {
      ...base,
      ...v,
      ...style
    }
  }, icon, children);
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Button.jsx", error: String((e && e.message) || e) }); }

// components/content/PricingCard.jsx
try { (() => {
function PricingCard({
  name,
  price,
  oldPrice,
  period,
  features = [],
  cta = 'Inscribirme',
  featured = false,
  badge,
  onSelect
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'relative',
      background: '#fff',
      borderRadius: 'var(--radius-xl)',
      padding: '28px 24px',
      border: featured ? '2px solid var(--cef-naranja)' : '1px solid var(--cef-borde)',
      boxShadow: featured ? 'var(--shadow-lg)' : 'var(--shadow-sm)',
      fontFamily: 'var(--font-sans)',
      display: 'flex',
      flexDirection: 'column',
      gap: 16
    }
  }, (badge || featured) && /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'absolute',
      top: -13,
      left: 24
    }
  }, /*#__PURE__*/React.createElement(__ds_scope.Badge, {
    variant: featured ? 'gradient' : 'peach'
  }, badge || 'Más popular')), /*#__PURE__*/React.createElement("div", {
    style: {
      fontWeight: 700,
      fontSize: 18
    }
  }, name), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      alignItems: 'baseline',
      gap: 8
    }
  }, oldPrice && /*#__PURE__*/React.createElement("span", {
    style: {
      color: 'var(--cef-gris)',
      textDecoration: 'line-through',
      fontSize: 16
    }
  }, oldPrice), /*#__PURE__*/React.createElement("span", {
    style: {
      fontWeight: 900,
      fontSize: 40,
      letterSpacing: '-0.02em',
      color: featured ? 'var(--cef-naranja-700)' : 'var(--cef-tinta)'
    }
  }, price), period && /*#__PURE__*/React.createElement("span", {
    style: {
      color: 'var(--cef-gris)',
      fontSize: 14
    }
  }, period)), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gap: 10
    }
  }, features.map((f, i) => /*#__PURE__*/React.createElement(__ds_scope.CheckItem, {
    key: i
  }, f))), /*#__PURE__*/React.createElement(__ds_scope.Button, {
    variant: featured ? 'primary' : 'secondary',
    fullWidth: true,
    onClick: onSelect
  }, cta));
}
Object.assign(__ds_scope, { PricingCard });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/content/PricingCard.jsx", error: String((e && e.message) || e) }); }

// components/core/GradientText.jsx
try { (() => {
function GradientText({
  children,
  style
}) {
  return /*#__PURE__*/React.createElement("span", {
    style: {
      background: 'var(--gradient-estrella)',
      WebkitBackgroundClip: 'text',
      backgroundClip: 'text',
      color: 'transparent',
      WebkitTextFillColor: 'transparent',
      ...style
    }
  }, children);
}
Object.assign(__ds_scope, { GradientText });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/GradientText.jsx", error: String((e && e.message) || e) }); }

// components/core/Logo.jsx
try { (() => {
const files = {
  horizontal: 'logo-horizontal.png',
  vertical: 'logo-vertical.png',
  icon: 'icono.png'
};
function Logo({
  variant = 'horizontal',
  height = 32,
  basePath = 'assets/',
  style
}) {
  return /*#__PURE__*/React.createElement("img", {
    src: basePath + files[variant],
    alt: "Compra en f\xE1bricas",
    style: {
      height,
      width: 'auto',
      display: 'block',
      ...style
    }
  });
}
Object.assign(__ds_scope, { Logo });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Logo.jsx", error: String((e && e.message) || e) }); }

// components/forms/Checkbox.jsx
try { (() => {
function Checkbox({
  label,
  checked,
  defaultChecked = false,
  onChange,
  disabled
}) {
  const [c, setC] = React.useState(defaultChecked);
  const on = checked ?? c;
  return /*#__PURE__*/React.createElement("label", {
    style: {
      display: 'flex',
      gap: 10,
      alignItems: 'center',
      fontFamily: 'var(--font-sans)',
      fontSize: 15,
      cursor: disabled ? 'not-allowed' : 'pointer',
      opacity: disabled ? .5 : 1
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      flex: 'none',
      width: 22,
      height: 22,
      borderRadius: 6,
      background: on ? 'var(--gradient-estrella)' : '#fff',
      border: on ? 'none' : '1.5px solid var(--cef-borde)',
      color: '#fff',
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontSize: 13,
      fontWeight: 700
    }
  }, on ? '✓' : ''), /*#__PURE__*/React.createElement("input", {
    type: "checkbox",
    checked: on,
    disabled: disabled,
    onChange: e => {
      setC(e.target.checked);
      onChange && onChange(e.target.checked);
    },
    style: {
      display: 'none'
    }
  }), label);
}
Object.assign(__ds_scope, { Checkbox });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Checkbox.jsx", error: String((e && e.message) || e) }); }

// components/forms/Input.jsx
try { (() => {
function Input({
  label,
  placeholder,
  type = 'text',
  value,
  onChange,
  error,
  hint,
  disabled
}) {
  const [f, setF] = React.useState(false);
  return /*#__PURE__*/React.createElement("label", {
    style: {
      display: 'grid',
      gap: 6,
      fontFamily: 'var(--font-sans)'
    }
  }, label && /*#__PURE__*/React.createElement("span", {
    style: {
      fontWeight: 700,
      fontSize: 14
    }
  }, label), /*#__PURE__*/React.createElement("input", {
    type: type,
    placeholder: placeholder,
    value: value,
    onChange: onChange,
    disabled: disabled,
    onFocus: () => setF(true),
    onBlur: () => setF(false),
    style: {
      ...{
        display: 'block',
        width: '100%',
        fontFamily: 'var(--font-sans)',
        fontSize: 16,
        padding: '14px 16px',
        borderRadius: 'var(--radius-md)',
        background: '#fff',
        color: 'var(--cef-tinta)',
        outline: 'none',
        transition: 'border-color var(--dur-fast),box-shadow var(--dur-fast)'
      },
      border: '1.5px solid ' + (error ? 'var(--cef-naranja-700)' : f ? 'var(--cef-naranja)' : 'var(--cef-borde)'),
      boxShadow: f ? '0 0 0 4px rgba(249,115,22,.15)' : 'none',
      opacity: disabled ? .5 : 1
    }
  }), (error || hint) && /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 13,
      color: error ? 'var(--cef-naranja-700)' : 'var(--cef-gris)'
    }
  }, error || hint));
}
Object.assign(__ds_scope, { Input });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Input.jsx", error: String((e && e.message) || e) }); }

// components/forms/Radio.jsx
try { (() => {
function Radio({
  options = [],
  value,
  defaultValue,
  onChange,
  name = 'radio'
}) {
  const [v, setV] = React.useState(defaultValue);
  const cur = value ?? v;
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gap: 10,
      fontFamily: 'var(--font-sans)'
    }
  }, options.map(o => {
    const on = cur === o;
    return /*#__PURE__*/React.createElement("label", {
      key: o,
      style: {
        display: 'flex',
        gap: 12,
        alignItems: 'center',
        padding: '14px 16px',
        borderRadius: 'var(--radius-md)',
        border: '1.5px solid ' + (on ? 'var(--cef-naranja)' : 'var(--cef-borde)'),
        background: on ? 'var(--cef-crema)' : '#fff',
        cursor: 'pointer',
        fontSize: 15,
        fontWeight: on ? 700 : 400
      }
    }, /*#__PURE__*/React.createElement("span", {
      style: {
        flex: 'none',
        width: 20,
        height: 20,
        borderRadius: 999,
        border: '2px solid ' + (on ? 'var(--cef-naranja)' : 'var(--cef-borde)'),
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center'
      }
    }, on && /*#__PURE__*/React.createElement("span", {
      style: {
        width: 10,
        height: 10,
        borderRadius: 999,
        background: 'var(--gradient-estrella)'
      }
    })), /*#__PURE__*/React.createElement("input", {
      type: "radio",
      name: name,
      checked: on,
      onChange: () => {
        setV(o);
        onChange && onChange(o);
      },
      style: {
        display: 'none'
      }
    }), o);
  }));
}
Object.assign(__ds_scope, { Radio });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Radio.jsx", error: String((e && e.message) || e) }); }

// components/forms/Select.jsx
try { (() => {
function Select({
  label,
  options = [],
  value,
  onChange,
  placeholder
}) {
  const [f, setF] = React.useState(false);
  return /*#__PURE__*/React.createElement("label", {
    style: {
      display: 'grid',
      gap: 6,
      fontFamily: 'var(--font-sans)'
    }
  }, label && /*#__PURE__*/React.createElement("span", {
    style: {
      fontWeight: 700,
      fontSize: 14
    }
  }, label), /*#__PURE__*/React.createElement("select", {
    value: value,
    onChange: onChange,
    onFocus: () => setF(true),
    onBlur: () => setF(false),
    style: {
      ...{
        display: 'block',
        width: '100%',
        fontFamily: 'var(--font-sans)',
        fontSize: 16,
        padding: '14px 16px',
        borderRadius: 'var(--radius-md)',
        background: '#fff',
        color: 'var(--cef-tinta)',
        outline: 'none',
        transition: 'border-color var(--dur-fast),box-shadow var(--dur-fast)'
      },
      appearance: 'none',
      paddingRight: 40,
      border: '1.5px solid ' + (f ? 'var(--cef-naranja)' : 'var(--cef-borde)'),
      boxShadow: f ? '0 0 0 4px rgba(249,115,22,.15)' : 'none',
      backgroundImage: 'linear-gradient(45deg,transparent 50%,#EA580C 50%),linear-gradient(135deg,#EA580C 50%,transparent 50%)',
      backgroundPosition: 'calc(100% - 22px) 50%,calc(100% - 16px) 50%',
      backgroundSize: '6px 6px',
      backgroundRepeat: 'no-repeat'
    }
  }, placeholder && /*#__PURE__*/React.createElement("option", {
    value: ""
  }, placeholder), options.map(o => /*#__PURE__*/React.createElement("option", {
    key: o,
    value: o
  }, o))));
}
Object.assign(__ds_scope, { Select });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Select.jsx", error: String((e && e.message) || e) }); }

// ui_kits/landing/Landing.jsx
try { (() => {
const {
  Button,
  Badge,
  GradientText,
  Logo,
  PeachBox,
  Card,
  CheckItem,
  PricingCard,
  Accordion
} = window.CompraEnFBricasDesignSystem_e5b2dc;
function LandingHeader({
  onCta
}) {
  return /*#__PURE__*/React.createElement("header", {
    style: {
      position: 'sticky',
      top: 0,
      zIndex: 5,
      background: 'rgba(255,248,245,.92)',
      backdropFilter: 'blur(10px)',
      borderBottom: '1px solid var(--cef-borde)',
      padding: '12px 20px',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement(Logo, {
    height: 30,
    basePath: "../../assets/"
  }), /*#__PURE__*/React.createElement(Button, {
    size: "sm",
    onClick: onCta
  }, "Registrarme"));
}
function Hero({
  onCta
}) {
  return /*#__PURE__*/React.createElement("section", {
    style: {
      padding: '32px 20px 8px',
      display: 'grid',
      gap: 18
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(Badge, null, "\uD83D\uDD34 Clase en vivo \xB7 gratis")), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontSize: 38,
      lineHeight: 1.05
    }
  }, "Aprende a comprar directo en ", /*#__PURE__*/React.createElement(GradientText, null, "f\xE1bricas de China"), " \uD83C\uDDE8\uD83C\uDDF3"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: 18,
      color: 'var(--cef-gris)'
    }
  }, "Te ense\xF1o paso a paso c\xF3mo encontrar proveedores confiables, negociar precios y traer tu primera importaci\xF3n sin intermediarios."), /*#__PURE__*/React.createElement("div", {
    style: {
      borderRadius: 24,
      overflow: 'hidden',
      aspectRatio: '4/3.4',
      background: 'var(--cef-durazno)'
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/photos/eduardo-interior.jpg",
    style: {
      width: '100%',
      height: '100%',
      objectFit: 'cover',
      objectPosition: '62% 20%'
    }
  })), /*#__PURE__*/React.createElement(Button, {
    size: "lg",
    fullWidth: true,
    onClick: onCta
  }, "Quiero mi lugar gratis"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: 14,
      color: 'var(--cef-gris)',
      textAlign: 'center'
    }
  }, "Jueves 16 de octubre \xB7 7:00 pm (CDMX)"));
}
function Learn() {
  const items = ['Dónde encontrar fábricas verificadas', 'Cómo pedir muestras sin perder dinero', 'Cómo negociar precio y cantidad mínima', 'Cómo calcular envío e impuestos'];
  return /*#__PURE__*/React.createElement("section", {
    style: {
      padding: '40px 20px',
      display: 'grid',
      gap: 18
    }
  }, /*#__PURE__*/React.createElement(Badge, {
    style: {
      justifySelf: 'start'
    }
  }, "Lo que vas a aprender"), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: 28
    }
  }, "En 90 minutos sales con un ", /*#__PURE__*/React.createElement(GradientText, null, "plan claro")), /*#__PURE__*/React.createElement(Card, null, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gap: 14
    }
  }, items.map(i => /*#__PURE__*/React.createElement(CheckItem, {
    key: i
  }, i)))), /*#__PURE__*/React.createElement(PeachBox, {
    title: "Importante"
  }, "La clase es en vivo y no queda grabada. Con\xE9ctate 10 minutos antes."));
}
function Gift() {
  return /*#__PURE__*/React.createElement("section", {
    style: {
      padding: '0 20px 40px'
    }
  }, /*#__PURE__*/React.createElement(Card, {
    tone: "peach",
    padding: 24
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gap: 10
    }
  }, /*#__PURE__*/React.createElement(Badge, {
    variant: "gradient",
    style: {
      justifySelf: 'start'
    }
  }, "Regalo de bienvenida"), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontSize: 22
    }
  }, "Gu\xEDa: 50 f\xE1bricas verificadas \uD83C\uDDE8\uD83C\uDDF3"), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--cef-tinta)'
    }
  }, "Al registrarte recibes el material por WhatsApp."))));
}
function About() {
  return /*#__PURE__*/React.createElement("section", {
    style: {
      background: '#fff',
      padding: '40px 20px',
      display: 'grid',
      gap: 16,
      borderTop: '1px solid var(--cef-borde)',
      borderBottom: '1px solid var(--cef-borde)'
    }
  }, /*#__PURE__*/React.createElement(Badge, {
    style: {
      justifySelf: 'start'
    }
  }, "Qui\xE9n te ense\xF1a"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 16,
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/photos/eduardo-exterior.jpg",
    style: {
      width: 84,
      height: 84,
      borderRadius: 999,
      objectFit: 'cover',
      objectPosition: '50% 20%'
    }
  }), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h3", {
    style: {
      fontSize: 22
    }
  }, "Eduardo"), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--cef-gris)',
      fontSize: 15
    }
  }, "Fundador de Compra en f\xE1bricas"))), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: 16
    }
  }, "Llevo a\xF1os comprando directo en f\xE1bricas de China. Hoy te comparto el proceso exacto que uso, sin rodeos."));
}
function Plans({
  onCta
}) {
  return /*#__PURE__*/React.createElement("section", {
    style: {
      padding: '48px 20px',
      display: 'grid',
      gap: 28
    }
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: 28,
      textAlign: 'center'
    }
  }, "\xBFQuieres ir ", /*#__PURE__*/React.createElement(GradientText, null, "m\xE1s r\xE1pido?")), /*#__PURE__*/React.createElement(PricingCard, {
    name: "Mentor\xEDa Importa Ya",
    price: "$297",
    oldPrice: "$497",
    period: "USD",
    featured: true,
    features: ['8 clases en vivo', 'Lista de fábricas verificadas', 'Acompañamiento en tu primer pedido', 'Grupo privado 🇨🇳'],
    cta: "Inscribirme ahora",
    onSelect: onCta
  }), /*#__PURE__*/React.createElement(PricingCard, {
    name: "Curso grabado",
    price: "$97",
    period: "USD",
    features: ['12 lecciones', 'Plantillas de negociación', 'Acceso de por vida'],
    cta: "Elegir curso",
    onSelect: onCta
  }));
}
function Faq() {
  return /*#__PURE__*/React.createElement("section", {
    style: {
      padding: '0 20px 48px',
      display: 'grid',
      gap: 16
    }
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: 26
    }
  }, "Preguntas frecuentes"), /*#__PURE__*/React.createElement(Accordion, {
    defaultOpen: 0,
    items: [{
      q: '¿Necesito tener empresa?',
      a: 'No. Puedes empezar como persona física y formalizar después.'
    }, {
      q: '¿Cuánto necesito invertir?',
      a: 'Te muestro cómo empezar con pedidos pequeños y muestras.'
    }, {
      q: '¿La clase queda grabada?',
      a: 'No. Es en vivo, por eso te pedimos conectarte a tiempo.'
    }]
  }));
}
function Footer() {
  return /*#__PURE__*/React.createElement("footer", {
    style: {
      background: 'var(--cef-tinta)',
      color: '#fff',
      padding: '32px 20px',
      display: 'grid',
      gap: 10,
      textAlign: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      background: '#fff',
      borderRadius: 12,
      padding: '8px 12px'
    }
  }, /*#__PURE__*/React.createElement(Logo, {
    height: 24,
    basePath: "../../assets/"
  }))), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: 13,
      color: '#bbb'
    }
  }, "\xA9 2026 Compra en f\xE1bricas \uD83C\uDDE8\uD83C\uDDF3 \xB7 Aviso de privacidad"));
}
function LandingScreen({
  onCta
}) {
  return /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(LandingHeader, {
    onCta: onCta
  }), /*#__PURE__*/React.createElement(Hero, {
    onCta: onCta
  }), /*#__PURE__*/React.createElement(Learn, null), /*#__PURE__*/React.createElement(Gift, null), /*#__PURE__*/React.createElement(About, null), /*#__PURE__*/React.createElement(Plans, {
    onCta: onCta
  }), /*#__PURE__*/React.createElement(Faq, null), /*#__PURE__*/React.createElement(Footer, null));
}
Object.assign(window, {
  LandingScreen,
  LandingHeader,
  Footer
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/landing/Landing.jsx", error: String((e && e.message) || e) }); }

// ui_kits/landing/Register.jsx
try { (() => {
const {
  Button: RB,
  Badge: RBadge,
  GradientText: RG,
  Input,
  Select,
  Checkbox,
  Radio,
  PeachBox: RPB,
  Card: RCard,
  Logo: RLogo
} = window.CompraEnFBricasDesignSystem_e5b2dc;
function RegisterScreen({
  onBack,
  onDone
}) {
  const [name, setName] = React.useState('');
  return /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: '100%'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      padding: '14px 20px',
      display: 'flex',
      alignItems: 'center',
      gap: 12,
      borderBottom: '1px solid var(--cef-borde)',
      background: '#fff'
    }
  }, /*#__PURE__*/React.createElement("button", {
    onClick: onBack,
    style: {
      all: 'unset',
      cursor: 'pointer',
      fontSize: 22,
      color: 'var(--cef-naranja-700)',
      fontWeight: 700
    }
  }, "\u2190"), /*#__PURE__*/React.createElement(RLogo, {
    height: 26,
    basePath: "../../assets/"
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      padding: '28px 20px',
      display: 'grid',
      gap: 18
    }
  }, /*#__PURE__*/React.createElement(RBadge, {
    style: {
      justifySelf: 'start'
    }
  }, "\uD83D\uDD34 Clase en vivo"), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontSize: 30
    }
  }, "Aparta tu lugar ", /*#__PURE__*/React.createElement(RG, null, "gratis")), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--cef-gris)'
    }
  }, "Te enviamos el link de acceso y tu regalo de bienvenida por WhatsApp."), /*#__PURE__*/React.createElement(RCard, null, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gap: 14
    }
  }, /*#__PURE__*/React.createElement(Input, {
    label: "Nombre",
    placeholder: "Tu nombre",
    value: name,
    onChange: e => setName(e.target.value)
  }), /*#__PURE__*/React.createElement(Input, {
    label: "WhatsApp",
    placeholder: "+52 55 1234 5678"
  }), /*#__PURE__*/React.createElement(Select, {
    label: "Pa\xEDs",
    placeholder: "Elige tu pa\xEDs",
    options: ['México', 'Colombia', 'Perú', 'Chile', 'Argentina', 'Estados Unidos']
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      fontWeight: 700,
      fontSize: 14
    }
  }, "\xBFYa has importado antes?"), /*#__PURE__*/React.createElement(Radio, {
    name: "exp",
    defaultValue: "Nunca he importado",
    options: ['Nunca he importado', 'Ya importé 1 vez', 'Importo seguido']
  }), /*#__PURE__*/React.createElement(Checkbox, {
    label: "Quiero recibir la gu\xEDa por WhatsApp",
    defaultChecked: true
  }))), /*#__PURE__*/React.createElement(RB, {
    size: "lg",
    fullWidth: true,
    onClick: () => onDone(name)
  }, "Confirmar mi lugar"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: 13,
      color: 'var(--cef-gris)',
      textAlign: 'center'
    }
  }, "Tus datos est\xE1n seguros. Nunca enviamos spam.")));
}
function ThanksScreen({
  name,
  onBack
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      padding: '48px 20px',
      display: 'grid',
      gap: 20,
      textAlign: 'center',
      justifyItems: 'center'
    }
  }, /*#__PURE__*/React.createElement(RLogo, {
    variant: "icon",
    height: 64,
    basePath: "../../assets/"
  }), /*#__PURE__*/React.createElement(RBadge, {
    variant: "success"
  }, "Registro confirmado"), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontSize: 32
    }
  }, "\xA1Listo", name ? ', ' + name : '', "! ", /*#__PURE__*/React.createElement(RG, null, "Ya tienes tu lugar"), " \uD83C\uDDE8\uD83C\uDDF3"), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--cef-gris)',
      fontSize: 17
    }
  }, "En unos minutos te llega por WhatsApp el link de la clase y tu gu\xEDa de 50 f\xE1bricas verificadas."), /*#__PURE__*/React.createElement(RPB, {
    title: "\xDAltimo paso",
    style: {
      textAlign: 'left',
      width: '100%'
    }
  }, "Agrega nuestro n\xFAmero a tus contactos para que el mensaje no se pierda."), /*#__PURE__*/React.createElement(RB, {
    variant: "secondary",
    fullWidth: true,
    onClick: onBack
  }, "Volver al inicio"));
}
Object.assign(window, {
  RegisterScreen,
  ThanksScreen
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/landing/Register.jsx", error: String((e && e.message) || e) }); }

__ds_ns.Accordion = __ds_scope.Accordion;

__ds_ns.Card = __ds_scope.Card;

__ds_ns.CheckItem = __ds_scope.CheckItem;

__ds_ns.PeachBox = __ds_scope.PeachBox;

__ds_ns.PricingCard = __ds_scope.PricingCard;

__ds_ns.Badge = __ds_scope.Badge;

__ds_ns.Button = __ds_scope.Button;

__ds_ns.GradientText = __ds_scope.GradientText;

__ds_ns.Logo = __ds_scope.Logo;

__ds_ns.Checkbox = __ds_scope.Checkbox;

__ds_ns.Input = __ds_scope.Input;

__ds_ns.Radio = __ds_scope.Radio;

__ds_ns.Select = __ds_scope.Select;

})();
