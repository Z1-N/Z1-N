
# GitHub Authentication Methods

GitHub supports multiple authentication methods to securely access your repositories. This guide covers the two most common and secure methods:

- [Personal Access Token (PAT)](#1-authentication-via-personal-access-token-pat)
- [SSH Key Authentication](#2-authentication-via-ssh-key)

---

## 1. Authentication via Personal Access Token (PAT)

Since August 13, 2021, GitHub no longer supports password authentication for Git operations. Instead, **Personal Access Tokens (PATs)** are used.

### ✅ Use Cases
- HTTPS cloning and pushing
- GitHub API access

### 🔐 How to Create a Personal Access Token

1. Go to [GitHub Developer Settings](https://github.com/settings/tokens).
2. Click on `Generate new token`.
3. Select the appropriate scopes (e.g., `repo`, `workflow`, `admin:org`, etc.).
4. Set an expiration date and generate the token.
5. Copy the token and **store it securely**. You won't be able to view it again.

### 🔧 Using PAT with Git

#### Clone a repository:
```bash
git clone https://github.com/username/repo.git
```

When prompted for a username and password:
- Use your **GitHub username**
- Paste the **PAT** as the password

#### Configure Git to remember your token:
```bash
git config --global credential.helper store
```

> This stores credentials in plain text, use with caution. For a more secure option, use `credential-manager-core` (Windows/macOS) or `git-credential-libsecret` (Linux).

---

## 2. Authentication via SSH Key

SSH is a secure and convenient method that avoids repeated prompts for your credentials.

### ✅ Use Cases
- Cloning/pushing via SSH
- Automating Git operations in scripts/CI pipelines

### 🔧 Generate and Add SSH Key

#### 1. Generate SSH Key Pair
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

> If `ed25519` is not supported, use:
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Follow the prompts and choose a secure passphrase.

#### 2. Start SSH Agent and Add Key
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

#### 3. Add Public Key to GitHub

1. Copy the public key:
```bash
cat ~/.ssh/id_ed25519.pub
```

2. Go to [GitHub SSH Settings](https://github.com/settings/keys).
3. Click `New SSH Key`, paste the key, and save.

#### 4. Test SSH Connection
```bash
ssh -T git@github.com
```

You should see:
```
Hi username! You've successfully authenticated...
```

### 🔗 Clone via SSH
```bash
git clone git@github.com:username/repo.git
```

---

## 🔄 Switching Between HTTPS and SSH

To change an existing repo's remote URL:

- From HTTPS to SSH:
```bash
git remote set-url origin git@github.com:username/repo.git
```

- From SSH to HTTPS:
```bash
git remote set-url origin https://github.com/username/repo.git
```

---

## 🛠️ Tips and Best Practices

- Use **SSH** for long-term development and automation.
- Use **PAT** when working with GitHub API or via HTTPS.
- Rotate your PAT regularly and avoid hardcoding it in code.
- Use SSH key passphrases and a key agent for security.
- Avoid using your main PAT in CI/CD; instead, create a **fine-scoped token** or use **GitHub Actions secrets**.

---

## 📚 Resources

- [GitHub Docs: PATs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [GitHub Docs: SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [Git Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage)
